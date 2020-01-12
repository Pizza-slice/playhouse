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
        private ClientConnection clientConnection;
        public Form1(ClientConnection clientConnection)
        {
            this.clientConnection = clientConnection;
            InitializeComponent();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            String search_qurey = textBox1.Text;
            this.clientConnection.Send(search_qurey);

        }
    }
}
