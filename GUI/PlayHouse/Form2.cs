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
        private String CACHE_DIR = @"D:\Users\User\playhouse\API\api_client";

        public Form2(ClientHandler c, JObject jsonData)
        {
            InitializeComponent();
            this.clientHandler = c;
            this.jsonData = jsonData.Value<JObject>("album");
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            String path = clientHandler.GetCoverImage(this.jsonData.Value<String>("coverImage"));
            pictureBox1.ImageLocation = this.CACHE_DIR + "\\" + path;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            
            
        }
    }
}
