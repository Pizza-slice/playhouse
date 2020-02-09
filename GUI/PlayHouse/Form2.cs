using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PlayHouse
{
    public partial class Form2 : Form
    {
        private ClientHandler clientHandler;
        private JObject jsonData;
        private List<Song> songList;

        public Form2(ClientHandler c, JObject jsonData)
        {
            InitializeComponent();
            this.clientHandler = c;
            this.jsonData = jsonData.Value<JObject>("album");
            this.songList = new List<Song>();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            label1.Text = this.jsonData.Value<String>("name");
            label3.Text = this.clientHandler.GetJsonById(this.jsonData.Value<String>("artist"), "artist").Value<JObject>("artist").Value<String>("name");
            String path = clientHandler.GetCoverImage(this.jsonData.Value<String>("coverImage"));
            pictureBox1.Image = Image.FromFile(path);
            foreach(String id in this.jsonData.Value<JArray>("song_list").ToObject<List<String>>())
            {
                this.songList.Add(new Song(id, this.clientHandler));
            }
            listBox1.Items.AddRange(songList.Select(c => c.GetName()).ToArray());
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            String name = listBox1.GetItemText(listBox1.SelectedItem);
            Song song = this.songList.Find(songs => songs.GetName().Equals(name));
            this.clientHandler.StartStreaming(song.GetStreamingId());
        }
    }
    class Song
    {
        private String id;
        private JObject jsonData;
        public Song(String id, JObject jsonData)
        {
            this.id = id;
            this.jsonData = jsonData.Value<JObject>("song");
        }
        public Song(String id, ClientHandler c)
        {
            this.id = id;
            this.jsonData = c.GetJsonById(this.id, "song").Value<JObject>("song");
        }
        public String GetName()
        {
            return this.jsonData.Value<String>("name");
        }
        public String GetStreamingId()
        {
            return this.jsonData.Value<String>("streaming_id");
        }
    }
}
