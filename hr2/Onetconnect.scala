import java.sql.{DriverManager, Connection}
object OnetConnect{
	def main(args:Array[String]){
		val url = "jdbc:mysql://localhost:8889/mysql"
    	val driver = "com.mysql.jdbc.Driver"
    	val username = "root"
    	val password = "iiits_12345"
    	var connection:Connection = null
    	try {
        	Class.forName(driver)
        	connection = DriverManager.getConnection(url, username, password)
        	val statement = connection.createStatement
        	val rs = statement.executeQuery("SELECT host, user FROM user")
        	while (rs.next) {
        	    val host = rs.getString("host")
        	    val user = rs.getString("user")
        	    println("host = %s, user = %s".format(host,user))
        	}
    	} catch {
        	case e: Exception => e.printStackTrace
    	}
    	connection.close
	}
}