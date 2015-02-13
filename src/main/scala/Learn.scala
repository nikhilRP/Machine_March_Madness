import scala.io.Source

/**
 * Main class. It starts right here
 * Learn method to load the data and get the training started.
 *
 * Created by Nikhil on 2/12/15.
 */

object Learn {

  var teams: List[Map[String, String]] = List()
  var regularSeasonDataBySeason: List[Map[Int, Game]] = List()
  var tourneyDataBySeason: List[Map[Int, Game]] = List()
  var seasons: List[Int] = List(2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014)

  def main(args: Array[String]) = {

    println("Loading teams...")
    loadTeamCodes
    println("Number of teams loaded - " + teams.size)

    println("Loading regular season games...")
    loadRegularSeasonData

    println("Loading tourney data...")
    //loadTourneyData

    println("Summary of games loaded...")
    //printSeasonSummary
  }

  def loadTeamCodes = {
    new CSV().parse(getClass.getResource("teams.csv"), "UTF-8")
  }

  def loadRegularSeasonData() = {
    //new CSV().parse(Source.fromURL(getClass.getResource("regular_season_detailed_results.csv"), "UTF-8"))
  }

  def loadTourneyData() = {
    //tourneyDataBySeason = new CSV().parse(Source.fromURL(getClass.getResource("tourney_detailed_results.csv"), "UTF-8"))
  }

  def printSeasonSummary = {
    //println()
  }

}
