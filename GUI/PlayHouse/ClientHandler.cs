using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PlayHouse
{
    class ClientHandler
    {
        private ClientConnection c;
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
    }
        
}
