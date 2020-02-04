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
        private List<PlayableItem> itemList = new List<PlayableItem>();
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
                ClearList();
                this.itemList.AddRange(this.GetItemByID(response.Value<JArray>("album").ToObject<List<String>>(), "album"));
                this.itemList.AddRange(this.GetItemByID(response.Value<JArray>("artist").ToObject<List<String>>(), "artist"));
                this.itemList.AddRange(this.GetItemByID(response.Value<JArray>("song").ToObject<List<String>>(), "song"));
                this.UpdateItemList(itemList);
            }
            else
            {
                ClearList();
            }


        }
        public void UpdateItemList(List<PlayableItem> itemList)
        {
           foreach(PlayableItem item in itemList)
            {
                allList.Items.Add(item.GetName());
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
        public PlayableItem GetItemByName(String itemName)
        {
            foreach(PlayableItem item in this.itemList)
            {
                
                if (item.GetName().Equals(itemName))
                {
                    return item;
                }
            }
            return null;
        }
        public List<PlayableItem> GetItemByID(List<String> idList, String type)
        {
            List<PlayableItem> tempitemList = new List<PlayableItem>();
            foreach (String id in idList)
            {
                
                PlayableItem playbleitem = new PlayableItem(id, type);
                playbleitem.GetJsonById(this.clientHandler);
                tempitemList.Add(playbleitem);
            }
            return tempitemList;
        }
        public void ClearList()
        {
            allList.Items.Clear();
            song_list.Items.Clear();
            artist_list.Items.Clear();
            album_list.Items.Clear();
            this.itemList.Clear();
        }
        
        private void all_list_SelectedIndexChanged(object sender, EventArgs e)
        {
            string text = allList.GetItemText(allList.SelectedItem);
            PlayableItem item = this.GetItemByName(text);
            if (item.type.Equals("album"))
            {
                Form2 album = new Form2(this.clientHandler, item.GetJson());
                album.ShowDialog();
            }
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

        private void song_result_Click(object sender, EventArgs e)
        {

        }

        private void album_result_Click(object sender, EventArgs e)
        {

        }
    }
}
