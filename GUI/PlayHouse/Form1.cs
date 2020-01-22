using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PlayHouse
{
    public partial class Form1 : Form
    {
        private ClientHandler clientHandler;
        public Form1(ClientConnection c)
        {
            this.clientHandler = new ClientHandler(c);
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {
                JObject response = this.clientHandler.SendSearchQuery(textBox1.Text, "all");
                List<PlayableItem> itemList = new List<PlayableItem>();
                ClearList();
                itemList.AddRange(this.GetItemByID(response.Value<JArray>("album").ToObject<List<String>>(), "album"));
                itemList.AddRange(this.GetItemByID(response.Value<JArray>("artist").ToObject<List<String>>(), "artist"));
                itemList.AddRange(this.GetItemByID(response.Value<JArray>("song").ToObject<List<String>>(), "song"));
                this.UpdateItemList(itemList);



            }
            else
            {
                allList.Items.Clear();
                song_list.Items.Clear();
                artist_list.Items.Clear();
                album_list.Items.Clear();
            }


        }
        public void UpdateItemList(List<PlayableItem> itemList)
        {
           foreach(PlayableItem item in itemList)
            {
                allList.Items.Add(item.GetName());
                Console.WriteLine(item.GetType());
                if (item.GetType().Equals("album"))
                {
                    album_list.Items.Add(item.GetName());
                }
                else if (item.GetType().Equals("artist"))
                {
                    artist_list.Items.Add(item.GetName());
                }
                else if (item.GetType().Equals("song"))
                {
                    song_list.Items.Add(item.GetName());
                }
            }
        }
        public List<PlayableItem> GetItemByID(List<String> idList, String type)
        {
            List<PlayableItem> itemList = new List<PlayableItem>();
            foreach (String id in idList)
            {
                
                PlayableItem playbleitem = new PlayableItem(id, type);
                playbleitem.GetJsonById(this.clientHandler);
                itemList.Add(playbleitem);
            }
            return itemList;
        }
        public void ClearList()
        {
            allList.Items.Clear();
            song_list.Items.Clear();
            artist_list.Items.Clear();
            album_list.Items.Clear();
        }
        
        private void all_list_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void song_list_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        private void artist_list_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        private void album_list_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        private void all_result_click(object sender, EventArgs e)
        {
            
        }

        private void artist_result_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click_1(object sender, EventArgs e)
        {

        }
    }
}
