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
                all.Items.Clear();
                all.Items.Clear();
                song_list.Items.Clear();
                artist_list.Items.Clear();
                album_list.Items.Clear();
                all.Items.AddRange(this.GetNameById(response.Value<JArray>("album").ToObject<List<String>>().ToArray(), "album"));
                all.Items.AddRange(this.GetNameById(response.Value<JArray>("artist").ToObject<List<String>>().ToArray(), "artist"));
                all.Items.AddRange(this.GetNameById(response.Value<JArray>("song").ToObject<List<String>>().ToArray(), "song"));
                song_list.Items.AddRange(this.GetNameById(response.Value<JArray>("album").ToObject<List<String>>().ToArray(), "album"));
                artist_list.Items.AddRange(this.GetNameById(response.Value<JArray>("artist").ToObject<List<String>>().ToArray(), "artist"));
                album_list.Items.AddRange(this.GetNameById(response.Value<JArray>("song").ToObject<List<String>>().ToArray(), "song"));



            }
            else
            {
                all.Items.Clear();
                song_list.Items.Clear();
                artist_list.Items.Clear();
                album_list.Items.Clear();
            }


        }
        public String[] GetNameById(String[] idList, String type)
        {
            List<String> nameList = new List<string>();
            foreach (String id in idList)
            {
                JObject json_response = this.clientHandler.GetNameById(id, type);
                nameList.Add(json_response[type]["name"].ToString());
            }
            return nameList.ToArray();
        }
        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void listBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {

        }

        private void listBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
        private void label1_Click(object sender, EventArgs e)
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
