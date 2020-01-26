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
            this.allList = new System.Windows.Forms.ListBox();
            this.artist_list = new System.Windows.Forms.ListBox();
            this.song_list = new System.Windows.Forms.ListBox();
            this.album_list = new System.Windows.Forms.ListBox();
            this.all_result = new System.Windows.Forms.Label();
            this.artist_result = new System.Windows.Forms.Label();
            this.song_result = new System.Windows.Forms.Label();
            this.album_result = new System.Windows.Forms.Label();
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
            // allList
            // 
            this.allList.FormattingEnabled = true;
            this.allList.Items.AddRange(new object[] {
            " "});
            this.allList.Location = new System.Drawing.Point(251, 182);
            this.allList.Name = "allList";
            this.allList.Size = new System.Drawing.Size(345, 95);
            this.allList.TabIndex = 1;
            this.allList.SelectedIndexChanged += new System.EventHandler(this.all_list_SelectedIndexChanged);
            // 
            // artist_list
            // 
            this.artist_list.FormattingEnabled = true;
            this.artist_list.Items.AddRange(new object[] {
            " "});
            this.artist_list.Location = new System.Drawing.Point(251, 342);
            this.artist_list.Name = "artist_list";
            this.artist_list.Size = new System.Drawing.Size(345, 95);
            this.artist_list.TabIndex = 2;
            this.artist_list.SelectedIndexChanged += new System.EventHandler(this.artist_list_SelectedIndexChanged);
            // 
            // song_list
            // 
            this.song_list.FormattingEnabled = true;
            this.song_list.Items.AddRange(new object[] {
            " "});
            this.song_list.Location = new System.Drawing.Point(636, 182);
            this.song_list.Name = "song_list";
            this.song_list.Size = new System.Drawing.Size(345, 95);
            this.song_list.TabIndex = 3;
            this.song_list.SelectedIndexChanged += new System.EventHandler(this.song_list_SelectedIndexChanged);
            // 
            // album_list
            // 
            this.album_list.FormattingEnabled = true;
            this.album_list.Items.AddRange(new object[] {
            " "});
            this.album_list.Location = new System.Drawing.Point(636, 342);
            this.album_list.Name = "album_list";
            this.album_list.Size = new System.Drawing.Size(345, 95);
            this.album_list.TabIndex = 4;
            this.album_list.SelectedIndexChanged += new System.EventHandler(this.album_list_SelectedIndexChanged);
            // 
            // all_result
            // 
            this.all_result.AutoSize = true;
            this.all_result.Location = new System.Drawing.Point(248, 157);
            this.all_result.Name = "all_result";
            this.all_result.Size = new System.Drawing.Size(17, 13);
            this.all_result.TabIndex = 5;
            this.all_result.Text = "all";
            this.all_result.Click += new System.EventHandler(this.all_result_click);
            // 
            // artist_result
            // 
            this.artist_result.AutoSize = true;
            this.artist_result.Location = new System.Drawing.Point(248, 317);
            this.artist_result.Name = "artist_result";
            this.artist_result.Size = new System.Drawing.Size(29, 13);
            this.artist_result.TabIndex = 6;
            this.artist_result.Text = "artist";
            this.artist_result.Click += new System.EventHandler(this.artist_result_Click);
            // 
            // song_result
            // 
            this.song_result.AutoSize = true;
            this.song_result.Location = new System.Drawing.Point(633, 157);
            this.song_result.Name = "song_result";
            this.song_result.Size = new System.Drawing.Size(35, 13);
            this.song_result.TabIndex = 7;
            this.song_result.Text = "songs";
            this.song_result.Click += new System.EventHandler(this.song_result_Click);
            // 
            // album_result
            // 
            this.album_result.AutoSize = true;
            this.album_result.Location = new System.Drawing.Point(628, 317);
            this.album_result.Name = "album_result";
            this.album_result.Size = new System.Drawing.Size(40, 13);
            this.album_result.TabIndex = 8;
            this.album_result.Text = "albums";
            this.album_result.Click += new System.EventHandler(this.album_result_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1380, 783);
            this.Controls.Add(this.album_result);
            this.Controls.Add(this.song_result);
            this.Controls.Add(this.artist_result);
            this.Controls.Add(this.all_result);
            this.Controls.Add(this.album_list);
            this.Controls.Add(this.song_list);
            this.Controls.Add(this.artist_list);
            this.Controls.Add(this.allList);
            this.Controls.Add(this.textBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.ListBox allList;
        private System.Windows.Forms.ListBox artist_list;
        private System.Windows.Forms.ListBox song_list;
        private System.Windows.Forms.ListBox album_list;
        private System.Windows.Forms.Label all_result;
        private System.Windows.Forms.Label artist_result;
        private System.Windows.Forms.Label song_result;
        private System.Windows.Forms.Label album_result;
    }
}

