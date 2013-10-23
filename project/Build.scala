import sbt._

object Projects {
  lazy val twilio = RootProject(uri("git://github.com/daggerrz/Scwilio.git#d1931383d776601fd60d28dbc9e7c668083f6cfb"))
}

object MyBuild extends Build {
  lazy val root = Project("root", file("."))
                         .dependsOn(Projects.twilio)
}
