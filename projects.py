import os
import sys
import MySQLdb


class Project:
    ID = 0
    Name = 'Project1'
    Mantra = ''
    TaskCompletedCount = 0
    TaskTotalCount = 1
    Completion = 0
    Status = ['ready', 'doing', 'done'][0]


def get_list():
    sys.path.append(os.curdir)
    from dbconfig import db
    try:
        conn = MySQLdb.connect(
            host=db['host'],
            port=db['port'],
            user=db['user'],
            passwd=db['passwd'],
            database=db['database'],
            charset=db['charset'],
        )
    except MySQLdb.DatabaseError as err:
        print(err)
        print("Can't connect to database")
        return []
    c = conn.cursor()
    sql = '''SELECT
        t1.id, t1.name as project_name, t1.description,
        sum(CASE t3.title WHEN 'Done' THEN 1 WHEN '完成' THEN 1 ELSE 0 END) as task_completed,
        count(t2.id) as task_all
        FROM projects t1
            LEFT JOIN tasks t2 ON t1.id=t2.project_id
            LEFT JOIN `columns` t3 ON t2.column_id=t3.id
        WHERE t1.is_active=1 and t2.is_active=1
        GROUP BY t1.id;'''
    c.execute(sql)
    result = c.fetchall()
    conn.close()

    # fetchall 返回例子：((1, 'KaffaWeb.三合', Decimal('3'), 7),)
    # 其中 Decimal 需转化为 int
    project_list = []

    for t in result:
        project = Project()

        project.ID = t[0]
        project.Name = t[1]
        project.Mantra = str(t[2]).split(os.linesep)[0]
        project.TaskCompletedCount = int(t[3])
        project.TaskTotalCount = t[4]
        project.Completion = round(project.TaskCompletedCount / project.TaskTotalCount, 2)
        if project.TaskCompletedCount == 0:
            project.Status = 'ready'
        elif project.TaskCompletedCount < project.TaskTotalCount:
            project.Status = 'doing'
        elif project.TaskCompletedCount == project.TaskTotalCount:
            project.Status = 'done'

        project_list.append(project)

    return project_list


def main():
    for item in get_list():
        print('-' * 100)
        print('ID: ' + str(item.ID))
        print('Name: ' + item.Name)
        print('Mantra: ' + item.Mantra)
        print('TaskCompletedCount: ' + str(item.TaskCompletedCount))
        print('TaskTotalCount: ' + str(item.TaskTotalCount))
        print('Completion: ' + str(item.Completion))
        print('Status: ' + item.Status)


if __name__ == '__main__':
    main()

