namespace PlayHouse
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.all = new System.Windows.Forms.ListBox();
            this.artist_list = new System.Windows.Forms.ListBox();
            this.song_list = new System.Windows.Forms.ListBox();
            this.album_list = new System.Windows.Forms.ListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(251, 12);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(162, 20);
            this.textBox1.TabIndex = 0;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // all
            // 
            this.all.FormattingEnabled = true;
            this.all.Location = new System.Drawing.Point(251, 182);
            this.all.Name = "all";
            this.all.Size = new System.Drawing.Size(345, 95);
            this.all.TabIndex = 1;
            this.all.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged);
            // 
            // artist_list
            // 
            this.artist_list.FormattingEnabled = true;
            this.artist_list.Location = new System.Drawing.Point(251, 342);
            this.artist_list.Name = "artist_list";
            this.artist_list.Size = new System.Drawing.Size(345, 95);
            this.artist_list.TabIndex = 2;
            // 
            // song_list
            // 
            this.song_list.FormattingEnabled = true;
            this.song_list.Location = new System.Drawing.Point(636, 182);
            this.song_list.Name = "song_list";
            this.song_list.Size = new System.Drawing.Size(345, 95);
            this.song_list.TabIndex = 3;
            this.song_list.SelectedIndexChanged += new System.EventHandler(this.listBox1_SelectedIndexChanged_1);
            // 
            // album_list
            // 
            this.album_list.FormattingEnabled = true;
            this.album_list.Location = new System.Drawing.Point(636, 342);
            this.album_list.Name = "album_list";
            this.album_list.Size = new System.Drawing.Size(345, 95);
            this.album_list.TabIndex = 4;
            this.album_list.SelectedIndexChanged += new System.EventHandler(this.listBox2_SelectedIndexChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(248, 152);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(35, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "label1";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1380, 783);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.album_list);
            this.Controls.Add(this.song_list);
            this.Controls.Add(this.artist_list);
            this.Controls.Add(this.all);
            this.Controls.Add(this.textBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.ListBox all;
        private System.Windows.Forms.ListBox artist_list;
        private System.Windows.Forms.ListBox song_list;
        private System.Windows.Forms.ListBox album_list;
        private System.Windows.Forms.Label label1;
    }
}

