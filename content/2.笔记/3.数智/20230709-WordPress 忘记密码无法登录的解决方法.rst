WordPress 忘记密码无法登录的解决方法
##################################################

:date: 2023-07-09 17:40
:modified: 2024-07-09 23:39
:author: Kaffa
:category: digital
:tags: wordpress,password
:slug: solution-for-forget-wordpress-password
:summary: 本文提供一种从 WordPress 数据库直接修改密码的办法来解决忘记密码无法登录的问题。
:growth: 5

适用场景
====================

具有 WordPress 的数据库密码和权限，但忘记了 WordPress 密码。

解决办法
====================

假设用户名是 admin_username，在数据库中运行下面的 SQL::

    UPDATE wp_users SET user_pass=MD5('NEW_PASSWORD') WHERE wp_users.user_login='admin_username';


这条语句会将管理员密码更新为 MD5 加密字符串，此时，就可以使用 NEW_PASSWORD 登录，登录后，WordPress 会自动更新密码为新加密字符格式。


花絮
====================

从旧系统迁移过来，没想到整整一年了。
