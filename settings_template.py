from tornado.options import define

define("db_user", default="quicktalk", help="Database user name")
define("db_password", default=1234567, help="Password to database")
define("db_host", default="127.0.0.1", help="Database host")
define("db_name", default="quicktalk_db", help="Database name")


