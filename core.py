import database
import window

DBW=database.DBW()

#Comment these lines to keep previous iteration's DB, else remake from defaults.
import __makedefdb
__makedefdb.make(DBW)

if(window.Login(DBW)):
    window.EventLoop(DBW)
    DBW.DB.commit()