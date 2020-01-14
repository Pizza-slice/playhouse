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
            Dictionary<String,String> response =  this.clientHandler.SendSearchQuery(textBox1.Text, "album");
            Console.WriteLine(response);
        }
    }
}
