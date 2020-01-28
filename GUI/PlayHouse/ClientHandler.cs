using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PlayHouse
{
    public class ClientHandler
    {
        private ClientConnection c;
        private String cachePath = @"D:\Users\User\playhouse\GUI\PlayHouse\cache";
        public ClientHandler(ClientConnection c)
        {
            this.c = c;
        }
        public JObject SendSearchQuery(String query, String type)
        {
            Dictionary<string, string> json_request = new Dictionary<string, string>();
            json_request["endpoint"] = "search";
            json_request["q"] = query;
            json_request["type"] = type;
            c.Send(JsonConvert.SerializeObject(json_request));
            String json_response = c.Recv(1024);
            return JsonConvert.DeserializeObject<JObject>(json_response);
        }
        public JObject GetJsonById(String id, String type)
        {
            Dictionary<string, string> json_request = new Dictionary<string, string>();
            json_request["endpoint"] = type;
            json_request["q"] = id;
            c.Send(JsonConvert.SerializeObject(json_request));
            String json_response = c.Recv(1024);
            return JsonConvert.DeserializeObject<JObject>(json_response);
        }
        public void GetCoverImage(String coverImageId)
        {
            Dictionary<String, String> json_requst = new Dictionary<string, string>();
            json_requst["endpoint"] = "coverImage";
            json_requst["q"] = coverImageId;
            c.Send(JsonConvert.SerializeObject(json_requst));
            int data_length = JsonConvert.DeserializeObject<JObject>(c.Recv(1024)).Value<int>("data_length");
            c.Send("OK");
            String data = "";
            using (StreamWriter outputFile = new StreamWriterPath(this.cachePath +"\\temp.jpg"))
            {
                for (int i = 1; i <= data_length; i++)
                {
                    data = c.Recv(1024);
                    
                }
                if (data_length % 1024 != 0)
                    data = c.Recv(1024);
                fs.Write(Encoding.ASCII.GetBytes(data), 0, data_length % 1024);
            }
        }
    }
}
        
