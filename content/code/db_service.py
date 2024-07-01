# -*- coding: UTF-8 -*-
# 用途：更快管理本机 Postgres 和 MySQL / MariaDB 服务状态。（需要管理员权限）
# 作者: Kaffa
import subprocess
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import win32con
import win32service
import win32serviceutil

GAP = 10
WIN_WIDTH = 800
WIN_HEIGHT = 600
GROUPS = ('Postgres', 'MySQL', 'MariaDB')

tree = None


def get_services():
    return win32service.EnumServicesStatus(
        win32service.OpenSCManager(None, None, win32con.GENERIC_READ),
        win32service.SERVICE_WIN32,
        win32service.SERVICE_STATE_ALL)


def start_service(event):
    global tree

    item = tree.focus()
    service_name = tree.item(item, 'values')[0]

    try:
        win32serviceutil.StartService(service_name)
        messagebox.showinfo("提示", f"服务 {service_name} 已启动")
    except Exception as e:
        messagebox.showinfo("提示", f"启动服务 {service_name} 时出错: {e}")


def stop_service(event):
    global tree

    item = tree.focus()
    service_name = tree.item(item, 'values')[0]

    scm = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS)
    service = win32service.OpenService(scm, service_name, win32service.SERVICE_ALL_ACCESS)
    try:
        win32service.ControlService(service, win32service.SERVICE_CONTROL_STOP)
        messagebox.showinfo("提示", f"服务 {service_name} 已成功停止")
    except Exception as e:
        messagebox.showinfo("提示", f"停止服务 {service_name} 时出错: {e}")
    finally:
        win32service.CloseServiceHandle(service)
        win32service.CloseServiceHandle(scm)


def restart_service(event):
    stop_service(None)
    start_service(None)


def open_service(event):
    try:
        subprocess.Popen('services.msc', shell=True)
    except subprocess.CalledProcessError as e:
        print(f"执行命令时出错: {e}")


def enable_service(event):
    global tree
    item = tree.focus()
    service_name = tree.item(item, 'values')[0]
    scm = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS)
    service = win32service.OpenService(scm, service_name, win32service.SERVICE_ALL_ACCESS)
    try:
        win32service.ChangeServiceConfig(service,
                                         win32service.SERVICE_NO_CHANGE, win32service.SERVICE_AUTO_START,
                                         win32service.SERVICE_NO_CHANGE, None, None, 0, None, None, None, None)
        messagebox.showinfo("提示", f"服务 {service_name} 已成功启动")
    except Exception as e:
        messagebox.showinfo("提示", f"启用服务 {service_name} 时出错: {e}")
    finally:
        win32service.CloseServiceHandle(service)
        win32service.CloseServiceHandle(scm)


def disable_service(event):
    global tree

    item = tree.focus()
    service_name = tree.item(item, 'values')[0]
    scm = win32service.OpenSCManager(None, None, win32service.SC_MANAGER_ALL_ACCESS)
    service = win32service.OpenService(scm, service_name, win32service.SERVICE_ALL_ACCESS)
    try:
        win32service.ChangeServiceConfig(service,
                                         win32service.SERVICE_NO_CHANGE, win32service.SERVICE_DISABLED,
                                         win32service.SERVICE_NO_CHANGE, None, None, 0, None, None, None, None)
        messagebox.showinfo("提示", f"服务 {service_name} 已成功禁用")
    except Exception as e:
        messagebox.showinfo("提示", f"禁用服务 {service_name} 时出错: {e}")
    finally:
        win32service.CloseServiceHandle(service)
        win32service.CloseServiceHandle(scm)


def init_ctl(root):
    global tree
    frm = Frame(root, borderwidth=GAP, width=WIN_WIDTH, height=WIN_HEIGHT)
    frm.grid()

    Label(frm, text="Database Services").grid(column=0, row=0, columnspan=6, pady=GAP)

    btn_start = Button(frm, text="Start")
    btn_start.grid(column=0, row=1, pady=GAP)

    btn_stop = Button(frm, text="Stop")
    btn_stop.grid(column=1, row=1, pady=GAP)

    btn_restart = Button(frm, text="Restart")
    btn_restart.grid(column=2, row=1, pady=GAP)

    btn_enable = Button(frm, text="Enable")
    btn_enable.grid(column=3, row=1, pady=GAP)

    btn_disable = Button(frm, text="Disable")
    btn_disable.grid(column=4, row=1, pady=GAP)

    btn_service = Button(frm, text="Services")
    btn_service.grid(column=5, row=1, pady=GAP)

    services = get_services()
    tree = Treeview(frm, height=10, columns=('名称', '描述', '状态'), padding=GAP)
    tree.heading('名称', text='名称')
    tree.heading('描述', text='描述')
    tree.heading('状态', text='状态')
    for group in GROUPS:
        id_ = tree.insert('', END, iid=group.lower(), text=group, open=True)
        tree.column('名称', width=100, minwidth=100, )
        tree.column('描述', width=200, minwidth=200, )
        tree.column('状态', width=100, minwidth=100, )
        for (service_name, service_desc, service_status) in services:
            if group.lower() in service_name.lower():
                service_status_dict = {
                    win32service.SERVICE_CONTINUE_PENDING: "continue pending",
                    win32service.SERVICE_PAUSE_PENDING: "pause pending",
                    win32service.SERVICE_PAUSED: "paused",
                    win32service.SERVICE_RUNNING: "running",
                    win32service.SERVICE_START_PENDING: "start pending",
                    win32service.SERVICE_STOP_PENDING: "stop pending",
                    win32service.SERVICE_STOPPED: "stoped"

                }
                service_status = service_status_dict.get(service_status[1], "unknown")
                tree.insert(id_, END, values=(service_name, service_desc, service_status))
                tree.grid(column=0, row=2, columnspan=6, padx=GAP, pady=GAP)

    btn_start.bind(sequence="<Button-1>", func=start_service)
    btn_stop.bind(sequence="<Button-1>", func=stop_service)
    btn_restart.bind(sequence="<Button-1>", func=restart_service)
    btn_enable.bind(sequence="<Button-1>", func=enable_service)
    btn_disable.bind(sequence="<Button-1>", func=disable_service)
    btn_service.bind(sequence="<Button-1>", func=open_service)


def main():
    root = Tk()
    root.title('db service manager')

    w = WIN_WIDTH
    h = WIN_HEIGHT
    x = (root.winfo_screenwidth() - w) / 2
    y = (root.winfo_screenheight() - h) / 2
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))     # 宽x高+左+上

    init_ctl(root)

    root.mainloop()


if __name__ == '__main__':
    main()
