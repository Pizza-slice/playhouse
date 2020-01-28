using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PlayHouse
{
    public class PlayableItem
    {
        private String id;
        private String type;
        private JObject json;
        public PlayableItem(String Id, String type,JObject json)
        {
            this.id = Id;
            this.type = type;
            this.json = json;
        }
        public PlayableItem(String id, String type)
        {
            this.id = id;
            this.type = type;
            this.json = null;
        }
        public JObject GetJson()
        {
            return this.json;
        }
        public void GetJsonById(ClientHandler clientHandler)
        {
            this.json = clientHandler.GetJsonById(this.id, this.type);
        }
        public String GetName()
        {
            return this.json[this.type]["name"].ToString(); 
        }
        public new virtual String GetType()
        {
            return this.type;
        }
    }

}
