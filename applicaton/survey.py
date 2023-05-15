import creds    # this holds the database credentials - it is excluded from the repository
import pymysql.cursors
from flask import Flask, render_template, request

# init Flask 
app = Flask(__name__)

def connectdb():
    """
    Convenience function to connect to the database
    TODO: Would I be better holding one connection open using Flask.g rather then one per page?
    """
    return pymysql.connect(host=creds.host, user=creds.user, password=creds.password, 
        database=creds.database, charset=creds.charset, cursorclass=pymysql.cursors.DictCursor)


# reads results from qr code and loads agreement
@app.route("/")
def nowt():
    return f"<p>Nothing to see here...</p>"


# reads results from qr code and loads agreement
@app.route("/<town>/<park>")
def survey(town, park):
    
    # create connection
    connection = connectdb()

    # load user into database
    with connection:
        with connection.cursor() as cursor:
            
            # create a new user
            # create table `users` (`id_user` INT UNSIGNED NOT NULL AUTO_INCREMENT, `town` VARCHAR(64) NOT NULL, `park` VARCHAR(64) NOT NULL, `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id_user`));
            sql = "INSERT INTO `users` (`town`, `park`) VALUES (%s, %s)"
            cursor.execute(sql, (town, park))

        # commit changes to database
        connection.commit()
        
        # get user id
        userid = cursor.lastrowid

    # load next page
    return render_template('pis.html', userid=userid, town=town, park=park)


# reads results from qr code and loads agreement
@app.route("/s1", methods=['POST'])
def survey1():
    return render_template('s1.html', userid=request.form['userid'], town=request.form['town'], park=request.form['park'])


# reads results from qr code and loads agreement
@app.route("/s2", methods=['POST'])
def survey2():
    
    # create connection
    connection = connectdb()

    # load user into database
    with connection:
        with connection.cursor() as cursor:
        
            # load data from previous page into database
            # create table `people` (`id_user` INT UNSIGNED NOT NULL, `howoften` VARCHAR(64) NOT NULL, `perday` VARCHAR(64) NOT NULL, `startvisiting` VARCHAR(64) NOT NULL, `howlong` VARCHAR(64) NOT NULL, `timeofday` VARCHAR(64) NOT NULL, `dogs` VARCHAR(64) NOT NULL, `activity1` VARCHAR(64) NOT NULL, `activity2` VARCHAR(64) NOT NULL, `activity3` VARCHAR(64) NOT NULL, `activity4` VARCHAR(64) NOT NULL, `activity5` VARCHAR(64) NOT NULL, `activity6` VARCHAR(64) NOT NULL, `activity7` VARCHAR(64) NOT NULL, `activity8` VARCHAR(64) NOT NULL, `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id_user`));
            sql = "INSERT INTO `people` (`id_user`, `howoften`, `perday`, `startvisiting`, `howlong`, `timeofday`, `dogs`, `activity1`, `activity2`, `activity3`, \
                `activity4`, `activity5`, `activity6`, `activity7`, `activity8`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
                ON DUPLICATE KEY UPDATE `howoften` = %s, `perday` = %s, `startvisiting` = %s, `howlong` = %s, `timeofday` = %s, `dogs` = %s, `activity1` = %s, \
                    `activity2` = %s, `activity3` = %s, `activity4` = %s, `activity5` = %s, `activity6` = %s, `activity7` = %s, `activity8` = %s;"
            cursor.execute(sql, (int(request.form['userid']), 
                                 request.form['howoften'],
                                 request.form['perday'] if 'perday' in request.form else 'None',
                                 request.form['startvisiting'],
                                 request.form['howlong'],
                                 request.form['timeofday'],
                                 request.form['dogs'],
                                 request.form['activity1'] if 'activity1' in request.form else 'None',
                                 request.form['activity2'] if 'activity2' in request.form else 'None',
                                 request.form['activity3'] if 'activity3' in request.form else 'None',
                                 request.form['activity4'] if 'activity4' in request.form else 'None',
                                 request.form['activity5'] if 'activity5' in request.form else 'None',
                                 request.form['activity6'] if 'activity6' in request.form else 'None',
                                 request.form['activity7'] if 'activity7' in request.form else 'None',
                                 request.form['activity8'] if 'activity8' in request.form else 'None',  # repeated for 'on duplicate' after here
                                 request.form['howoften'],
                                 request.form['perday'] if 'perday' in request.form else 'None',
                                 request.form['startvisiting'],
                                 request.form['howlong'],
                                 request.form['timeofday'],
                                 request.form['dogs'],
                                 request.form['activity1'] if 'activity1' in request.form else 'None',
                                 request.form['activity2'] if 'activity2' in request.form else 'None',
                                 request.form['activity3'] if 'activity3' in request.form else 'None',
                                 request.form['activity4'] if 'activity4' in request.form else 'None',
                                 request.form['activity5'] if 'activity5' in request.form else 'None',
                                 request.form['activity6'] if 'activity6' in request.form else 'None',
                                 request.form['activity7'] if 'activity7' in request.form else 'None',
                                 request.form['activity8'] if 'activity8' in request.form else 'None'
                                 ))

        # commit changes to database
        connection.commit()

    # load next page
    return render_template('s2.html', userid=request.form['userid'], town=request.form['town'], park=request.form['park'], dog=request.form['dogs'])


# reads results from qr code and loads agreement
@app.route("/s3", methods=['POST'])
def survey3():
    
    # create connection
    connection = connectdb()

    # load user into database
    with connection:
        with connection.cursor() as cursor:
            
            # load data from previous page into database
            # create table `deer` (`id_user` INT UNSIGNED NOT NULL, `deer` VARCHAR(64) NOT NULL, `howoften` VARCHAR(64) NOT NULL, `lasttime` VARCHAR(64) NOT NULL, `howmany` VARCHAR(64) NOT NULL, `whatareas` VARCHAR(256) NOT NULL, `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id_user`));
            sql = "INSERT INTO `deer` (`id_user`, `deer`, `howoften`, `lasttime`, `howmany`, `whatareas`) VALUES (%s, %s, %s, %s, %s, %s) \
                ON DUPLICATE KEY UPDATE `deer` = %s, `howoften` = %s, `lasttime` = %s, `howmany` = %s, `whatareas` = %s;"
            cursor.execute(sql, (
                int(request.form['userid']), 
                request.form['deer'], 
                request.form['howoften'] if 'howoften' in request.form else 'None', 
                request.form['lasttime'] if 'lasttime' in request.form else 'None',
                request.form['howmany'] if 'howmany' in request.form else 'None',
                request.form['whatareas'],  # repeated for 'on duplicate' after here
                request.form['deer'], 
                request.form['howoften'] if 'howoften' in request.form else 'None', 
                request.form['lasttime'] if 'lasttime' in request.form else 'None',
                request.form['howmany'] if 'howmany' in request.form else 'None',
                request.form['whatareas'],
                ))

        # commit changes to database
        connection.commit()

    # load next page
    return render_template('s3.html', userid=request.form['userid'], town=request.form['town'], park=request.form['park'], dog=request.form['dog'])


# reads results from qr code and loads agreement
@app.route("/thankyou", methods=['POST'])
def thankyou():
    
    # create connection
    connection = connectdb()

    # load user into database
    with connection:
        with connection.cursor() as cursor:
            
            # create a new user
            # create table `ticks` (`id_user` INT UNSIGNED NOT NULL, `foundtick` VARCHAR(64) NOT NULL, `dogtick` VARCHAR(64) NOT NULL, `tickareas` VARCHAR(64) NOT NULL, `nattempts` INT NOT NULL, `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`id_user`));
            sql = "INSERT INTO `ticks` (`id_user`, `foundtick`, `dogtick`, `tickareas`, `nattempts`) VALUES (%s, %s, %s, %s, %s) \
                ON DUPLICATE KEY UPDATE `foundtick` = %s, `dogtick` = %s, `tickareas` = %s, `nattempts` = %s;"
            cursor.execute(sql, (
                int(request.form['userid']), 
                request.form['foundtick'],
                request.form['dogtick'],
                request.form['tickareas'],
                request.form['nattempts'],  # repeated for 'on duplicate' after here
                request.form['foundtick'],
                request.form['dogtick'],
                request.form['tickareas'],
                request.form['nattempts']
                ))

        # commit changes to database
        connection.commit()

    # load next page
    return render_template('thankyou.html')