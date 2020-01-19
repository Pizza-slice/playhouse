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
                all.Items.AddRange(response.Value<JArray>("album").ToObject<List<String>>().ToArray());
                all.Items.AddRange(response.Value<JArray>("artist").ToObject<List<String>>().ToArray());
                all.Items.AddRange(response.Value<JArray>("song").ToObject<List<String>>().ToArray());
                song_list.Items.AddRange(response.Value<JArray>("song").ToObject<List<String>>().ToArray());
                artist_list.Items.AddRange(response.Value<JArray>("artist").ToObject<List<String>>().ToArray());
                album_list.Items.AddRange(response.Value<JArray>("album").ToObject<List<String>>().ToArray());



            }
            else
            {
                all.Items.Clear();
                song_list.Items.Clear();
                artist_list.Items.Clear();
                album_list.Items.Clear();
            }


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
    }
}
