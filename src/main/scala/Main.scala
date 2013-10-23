import scwilio._


object Main extends App {
  val sid = "AC12fed9c7550c15932d433306163bfc91"
  val auth = "06b9d046a4afb08ab93262e4e3711eb7"

  val client = Twilio(sid, auth)
  client.sendSms(from = "+13023531770", to = "+13023539587", "Hello, there!")
}
