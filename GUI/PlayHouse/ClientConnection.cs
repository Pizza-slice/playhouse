using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net;
using System.Net.Sockets;
namespace PlayHouse
{
    public class ClientConnection
    {
        private Socket ClientSocket;
        public ClientConnection()
        {
            int port = this.StartClient();
            //int port = 3000;
            Console.WriteLine(port);
            IPAddress ipAddr = IPAddress.Parse("127.0.0.1");
            IPEndPoint localEndPoint = new IPEndPoint(ipAddr, port);
            this.ClientSocket = new Socket(ipAddr.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
            this.ClientSocket.Connect(localEndPoint);
        }
        int StartClient()
        {
            System.Diagnostics.Process p = new System.Diagnostics.Process();
            p.StartInfo.FileName = @"C:\cyber\anaconda3\python.exe";
            String port = this.GenerentePort();
            p.StartInfo.Arguments = @"D:\Users\User\playhouse\API\api_client\client.py " + port;
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardOutput = false;
            p.Start();
            return Convert.ToInt32(port);
        }
        String GenerentePort()
        {
            Random rnd = new Random();
            int port = rnd.Next(1000, 65535);
            return port.ToString();
        }
        public void Send(String Massage)
        {
            byte[] messageSent = Encoding.ASCII.GetBytes(Massage);
            int byteSent = this.ClientSocket.Send(messageSent);
        }
        public String Recv(int BufferSize)
        {
            byte[] messageReceived = new byte[BufferSize];
            int byteRecv = this.ClientSocket.Receive(messageReceived);
            return Encoding.ASCII.GetString(messageReceived, 0, byteRecv);

        }
        public void CloseConnection()
        {
            this.ClientSocket.Shutdown(SocketShutdown.Both);
            this.ClientSocket.Close();
        }
    }
}
