import discord
from discord import app_commands
from discord.ext import commands

import sqlite3
from datetime import datetime

class CollectStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.db_file = "stats.db"
        self.con = sqlite3.connect(self.db_file)
        self.cur = self.con.cursor()

        self.last_used_day = datetime.now().day
        self.tracker_day = 1

        self.last_used_hour = datetime.now().hour
        self.tracker_hour = 1

    @commands.Cog.listener()
    async def on_member_join(self, member):
        current_hour = datetime.now().hour
        current_day = datetime.now().day

        # Check if different hour
        if current_hour != self.last_used_hour:
            hour_difference = current_hour - self.last_used_hour

            # Check if different day
            if current_day != self.last_used_day:
                self.cur.execute("DELETE from total_members_daily")
                self.con.commit()

                # Pad hours
                hour_difference = current_hour
                self.last_used_hour = 0
                self.tracker_hour = 0

            # Update rows
            for hour in range(1, hour_difference + 1):
                self.cur.execute(f"INSERT into total_members_daily values ({self.last_used_hour + hour}, {0})")
            self.con.commit()
            self.tracker_hour += hour_difference

        member_count = self.cur.execute(f"SELECT members FROM total_members_daily WHERE hour = {self.tracker_hour}")
        member_count = member_count.fetchall()

        print(member_count)

        self.cur.execute(f"UPDATE total_members_daily SET members = {member_count + 1} WHERE hour = {self.tracker_hour}")
        self.con.commit()



async def setup(bot):
    await bot.add_cog(CollectStats(bot))