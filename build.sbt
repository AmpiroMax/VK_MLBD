ThisBuild / scalaVersion := "2.13.3"
ThisBuild / version := "0.0.1"

lazy val sample = (project in file("."))
  .settings(
    name := "hw3",

    libraryDependencies ++= Seq(
      "org.scalanlp" %% "breeze" % "2.1.0"
    )
  )
