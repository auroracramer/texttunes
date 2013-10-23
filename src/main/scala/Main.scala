import com.twilio.sdk.{TwilioRestClient, TwilioRestException}
import com.twilio.sdk.resource.factory.MessageFactory
import com.twilio.sdk.resource.instance.Message
import com.twilio.sdk.resource.list.MessageList
import org.apache.http.NameValuePair
import org.apache.http.message.BasicNameValuePair
import scala.collection.JavaConversions._
import scala.collection.mutable



object Main extends App {
  val sid = "AC12fed9c7550c15932d433306163bfc91"
  val auth = "06b9d046a4afb08ab93262e4e3711eb7"

  val client = new TwilioRestClient(sid, auth)
  //client.sendSms(from = "+13023531770", to = "+13023539587", "Hello, there!")
  val params = mutable.Buffer(
                   new BasicNameValuePair("Body", "Hello world!"),
                   new BasicNameValuePair("To", "+13023539587"),
                   new BasicNameValuePair("From", "13023531770"))

  val messageFactory = client.getAccount().getMessageFactory()
  val message = messageFactory.create(params)

}
