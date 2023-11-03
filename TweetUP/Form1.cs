using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;
using System.Collections.Generic;
using System.IO;

namespace TweetUP
{
    public partial class Form1 : Form
    {

        // variables
        string email;
        string pwd;

        public Form1()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            email = Email.Text;
            pwd = textBox1.Text;

            List<Person> people = new List<Person>();
            people.Add(new Person { emailData = email, PasswordDasta =  pwd});

            string json = JsonConvert.SerializeObject(people, Formatting.Indented);
            File.WriteAllText(@"./backend/credentials.json", json);
        }

        private void Email_TextChanged(object sender, EventArgs e)
        {

        }
    }
    public class Person
    {
        public string emailData { get; set; }
        public string PasswordDasta { get; set; }
    }

}
