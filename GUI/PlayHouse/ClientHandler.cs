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
        public String GetCoverImage(String coverImageId)
        {
            Dictionary<string, string> json_request = new Dictionary<string, string>();
            json_request["endpoint"] = "coverImage";
            json_request["q"] = coverImageId;
            c.Send(JsonConvert.SerializeObject(json_request));
            String json_response = c.Recv(1024);
            Console.WriteLine(json_response);
            return JsonConvert.DeserializeObject<JObject>(json_response).Value<String>("path");
        }
    }
}
        
