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
                response.Value<JArray>("artist").ToObject<List<String>>();

                response.Value<JArray>("album").ToObject<List<String>>();

                //listBox1.Items.AddRange();
                response.Value<JArray>("song").ToObject<List<String>>().ForEach((String song_id) =>
                {
                    foreach (String item in listBox1.Items)
                    {
                        if (item.ToString() != song_id)
                        {
                            listBox1.Items.Add(song_id);
                        }
                    }
                    if (listBox1.Items.Count == 0)
                    {
                        listBox1.Items.Add(song_id);
                    }
                });
            }


        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
