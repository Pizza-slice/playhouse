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
    public partial class Form2 : Form
    {
        private PlayableItem item;
        private ClientHandler clientHandler;
        public Form2(PlayableItem item, ClientHandler c)
        {
            InitializeComponent();
            this.item = item;
            this.clientHandler = c;
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            this.clientHandler.s
        }
        
    }
}
