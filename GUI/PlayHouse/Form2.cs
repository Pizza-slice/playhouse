using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using Newtonsoft.Json.Linq;

namespace PlayHouse
{  
    public partial class Form2 : Form
    {
        private PlayableItem item;
        private ClientHandler clientHandler;
        private String cachePath = @"D:\Users\User\playhouse\GUI\PlayHouse\cache";
        public Form2(PlayableItem item, ClientHandler c)
        {
            InitializeComponent();
            this.item = item;
            this.clientHandler = c;
        }
        private void Form2_Load(object sender, EventArgs e)
        {
            this.clientHandler.GetCoverImage(this.item.GetJson().Value<JObject>("album").Value<String>("coverImage"));
            pictureBox1.Image = Image.FromFile(this.cachePath + "\\temp.jpg");
            File.Delete(this.cachePath + "\\temp.jpg");
        }
        
    }
}
