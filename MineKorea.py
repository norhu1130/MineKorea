import discord
import asyncio
import datetime
import os

client = discord.Client()
app = discord.Client()
Setting = setting.Settings()

@app.event
async def on_ready():
    print("로그인을 끝냈습니다." % ())
    print("AmoBot은 현재 정상 가동중입니다!!!" % ())
    await app.change_presence(game=discord.Game(name="-도움말 | 베타 버전", type=0))
    print("플레이 중 세팅을 성공적으로 완료하였습니다." %())

@app.event
async def on_message(message):
    if message.author.bot or os.path.isfile("%s_Banned.rts" % (message.author.id)):
                   return None
                
                if "--공지설정" in message.content:
                    if message.author.id == Setting.owner_id:
                        f = open("notice_memo.rts", 'w')
                        f.write(message.content)
                        f.close()
                        await app.send_message(message.channel, "<@%s>, 공지 내용을 성공적으로 등록하였습니다!\n`--공지발신[channel id]`를 입력하여 공지를 보낼 수 있습니다." % (message.author.id))
                    else:
                        await app.send_message(message.channel, "<@%s>, 봇 관리자로 등록되어 있지 않습니다. `setting.py` 파일을 확인하여 주세요." % (message.author.id))

                if message.content.startswith('--공지발신'):
                    if message.author.id == Setting.owner_id:
                        q = open("notice_memo.rts", 'r').read()
                        q_channel = message.content[30:]
                        channel_info = app.get_channel(q_channel)
                        try:
                            await app.send_message(channel_info, q)
                            await app.send_message(message.channel, "<@%s>, 성공적으로 `%s`에 메시지를 보냈습니다!" % (message.author.id, channel_info))
                        except Exception as e:
                            await app.send_message(message.channel, "<@%s>, `%s`에 메시지를 보내지 못하였습니다.\n\n```%s```" % (message.author.id, channel_info, e))
                    else:
                        await app.send_message(message.channel, "<@%s>, 봇 관리자로 등록되어 있지 않습니다. `setting.py` 파일을 확인하여 주세요." % (message.author.id))

    
     
                if "--종료" == message.content:
                    if message.author.id == Setting.owner_id:
                        await app.send_message(message.channel, "<@%s>, 봇의 가동을 중지합니다. 5분 이내로 오프라인으로 전환됩니다(디스코드 API 딜레이)." % (message.author.id))
                        await app.change_presence(game=discord.Game(name="오프라인 전환중...사용을 중지해 주세요.", type=0))
                        quit() # 종료가성공적으로완료됌
                    else:
                        await app.send_message(message.channel, "<@%s>, 봇 관리자로 등록되어 있지 않습니다." % (message.author.id))
                
                if message.content.startswith('-사용소스'):
                  embed=discord.Embed(title="사용소스 내역입니다.", description=None, color=0x00ff00)
                  embed.add_field(name='Rutap open source', value='https://github.com/Team-Hwagong')
                  await app.send_message(message.channel, embed=embed) 

                if message.content.startswith('-봇프사'):
                  embed=discord.Embed(title='Bot profile photo', description=None, color=0x00ff00)
                  embed.add_field(name='Made by Ethan Kim the coder', value='봇의 프로필 사진입니다.')
                  await app.send_message(message.channel, embed=embed)
                  await app.send_message(message.channel, "https://cdn.discordapp.com/attachments/558971678583947264/559186971587510284/image0.png")

                if message.content.startswith("M 마크사이트"):
                  embed=discord.Embed(title='Mojang 사이트', description=None, color=0x00ff00)
                  embed.add_field(name='https://minecraft.net/ko-kr/?ref=m', value='마인크래프트 사이트입니다.')
                  await app.send_message(message.channel, embed=embed)

                if message.content.startswith('M 하이픽셀'):
                  embed=discord.Embed(title='Hypixel Network', desription=None, color=0x00ff00)
                  embed.add_field(name='MC.hypixel.net', value='하이픽셀은 개발자도 많이 겜하는 서버!')
                  await app.send_message(message.channel, embed=embed) 

                if message.content.startswith("M 온라인"):
                  embed=discord.Embed(title='온라인 상태', description=None, color=0x00ff00)
                  embed.add_field(name='I am online!', value='현재 온라인 상태입니다.')
                  await app.send_message(message.channel, embed=embed)  

                if message.content.startswith('M 도움말'):
                   embed=discord.Embed(title="MineKorea 도움말입니다.기본 접두사는 `M`입니다.", description=None, color=0x00ff00)
                   embed.add_field(name='M 봇프사', value='봇의 프로필 정보를 출력합니다. '  )
                   embed.add_field(name='M 사용소스', value='봇의 사용된 소스를 출력합니다. '  )
                   embed.add_field(name='M 마크사이트', value='마인크래프트 공식 사이트를 출력합니다.')
                   embed.add_field(name='M 온라인', value='봇이 온라인인지 확인합니다.메세지가 출력이 되지 않을 경우 오프라인입니다.')
                   embed.add_field(name='M 정보', value='봇의 정보를 출력합니다.')
                   embed.add_field(name='M 도움말', value='MK BOT의 명령어 전체를 출력합니다.')
                   embed.add_field(name='M 개발프로그램', value='개발 프로그램을 출력합니다.')
                   embed.add_field(name='M 아이디', value='당신의 유저아이디를 출력합니다.')
                   embed.add_field(name='M 개발자 정보', value='MK BOT 개발자 정보를 출력합니다.')
                   embed.add_field(name='MineKorea 개발자', value='Mine아모-Main #4899')
                   await app.send_message(message.author, embed=embed)

                if message.content.startswith('M 개발프로그램'):
                   embed=discord.Embed(title='개발 프로그램 내역입니다.', description=None, color=0x00ff00)
                   embed.add_field(name='언어', value='Python 3.5.4')
                   embed.add_field(name='소스 수정 프로그램', value='Visual Studio Code')
                   await app.send_message(message.channel, embed=embed)  

                if message.content.startswith('M 개발자명령어'):
                   if message.author.id == Setting.owner_id:
                    embed=discord.Embed()
                    embed.add_field(name='MK 공지', value='MineKorea 봇을 이용해 공지를 발신합니다.')  
                    embed.add_field(name='MK 공지설정', value='공지 내용을 등록합니다.')
                    embed.add_field(name='MK 공지발신', value='공지 내용을 발신합니다.')
                    embed.add_field(name='MK 종료', value='봇을 종료합니다.')  
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('M 아이디'):
                   embed=discord.Embed(title="당신의 유저 아이디 입니다.", color=0x00ff00)
                   embed.add_field(name=str(message.author.id), value='요청자 : ' + "<@" + str(message.author.id) + ">")
                   await app.send_message(message.channel, embed=embed)

                if message.content.startswith('M 개발자 정보'):
                   embed=discord.Embed(title='개발자 정보', description=None, color=0x00ff00)
                   embed.add_field(name='Mine아모-Main #4899', value='총개발자')
                   await app.send_message(message.channel, embed=embed)

                if message.content.startswith('M 정보'):
                    embed = discord.Embed(title="MineKorea 정보!", description=None, color=0x00ff00)
                    embed.add_field(name="[MineKorea 홈페이지]", value="https://minekorea.modoo.at/", inline=False)
                    embed.add_field(name="[MineKorea 개발자]", value="Mine아모-Main #4899", inline=False)
                    embed.add_field(name="[오픈소스 사용]", value="`M 사용소스`", inline=False)
                    embed.add_field(name="[MineKorea 공식 링크]", value="공식 카페 : https://cafe.naver.com/purplewqrxs\n공식 지원 디스코드 : https://discord.gg/hdHPjUA", inline=False)
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('M 사용서버'):
                   await app.send_message(message.channel, "사용된서버 %s" % (len(app.servers)))

                if message.channel.is_private:
                     await app.send_message(app.get_channel(Setting.err_log_channel), "문의도착!" + message.content + "사용자이름 : " + str(message.author.name) + "#" + str(message.author.discriminator))
                     embed=discord.Embed(title="DM 문의 전송", description=None, color=0x00ff00)
                     embed.add_field(name="DM 문의 전송 성공!", value="MineKorea 팀에게 문의가 전송되었습니다.", inline=True)
                     embed.add_field(name="지원서버 링크", value="https://discord.gg/hdHPjUA", inline=True)
                     await app.send_message(message.channel, embed=embed)

                if "M 문의" in message.content:
                     await app.send_message(app.get_channel(Setting.err_log_channel), "문의도착!" + message.content + "사용자이름 : " + str(message.author.name) + "#" + str(message.author.discriminator))
                     embed=discord.Embed(title='문의 발신 성공', color=0x00ff00)
                     embed.add_field(name='문의를 성공적으로 보냈습니다!', value='답장은 지원서버에서 받으실 수 있습니다.')
                     await app.send_message(message.author, embed=embed)

                if "M 서버정보" == message.content:
                    embed = discord.Embed(title="\"%s\" 서버정보!" % (message.server.name), description=None, color=Setting.embed_color)
                    embed.add_field(name="서버 소유자", value="<@%s>" % message.server.owner.id, inline=False)
                    embed.add_field(name="서버 생성일", value="%s (UTC)" % (message.server.created_at), inline=False)
                    embed.add_field(name="서버 보안등급", value=message.server.verification_level, inline=False)
                    embed.add_field(name="서버 위치", value=message.server.region, inline=False)
                    embed.add_field(name="서버 잠수채널", value="%s (%s분 이상 잠수이면 이동됨)" % (message.server.afk_channel, message.server.afk_timeout/60), inline=False)
                    embed.set_thumbnail(url=message.server.icon_url)
                    embed.set_footer(text = "Server ID : %s | Ver. %s | %s" % (message.server.id, Setting.version, Copyright))
                    await app.send_message(message.channel, embed=embed)

                if "M 핑" == message.content:
                    result = ping(message)
                    if result == False:
                        await app.send_message(message.channel, "<@" + message.author.id + ">,  서버의 안전을 위하여 상태를 한번에 여러명이 조회 할 수 없습니다!\n잠시 후 다시 시도 해 주세요!")
                    else:
                        embed = discord.Embed(title="루탑봇 상태!", description=None, color=Setting.embed_color)
                        if 0 < result < 400:
                            embed.add_field(name="서버 핑", value="`%sms`(:large_blue_circle: 핑이 정상입니다.)" % (str(result)), inline=False)
                            embed.add_field(name="봇 업타임", value="https://status.hwahyang.xyz/", inline=False)
                            embed.set_footer(text = "Ver. %s | %s" % (Setting.version, Copyright))
                            await app.send_message(message.channel, "<@%s>, " % (message.author.id), embed=embed)
                            os.remove("no_ping.rtl")
                        elif result > 399:
                            embed.add_field(name="서버 핑", value="`%sms`(:red_circle: 핑이 비정상입니다.)" % (str(result)), inline=False)
                            embed.add_field(name="봇 업타임", value="https://status.hwahyang.xyz/", inline=False)
                            embed.set_footer(text = "Ver. %s | %s" % (Setting.version, Copyright))
                            await app.send_message(message.channel, "<@%s>, " % (message.author.id), embed=embed)
                            os.remove("no_ping.rtl")
                        else:
                            embed.add_field(name="서버 핑", value="`%sms`(:question: 결과 도출 도중 문제가 발생했습니다.)" % (str(result)), inline=False)
                            embed.add_field(name="봇 업타임", value="https://status.hwahyang.xyz/", inline=False)
                            embed.set_footer(text = "Ver. %s | %s" % (Setting.version, Copyright))
                            await app.send_message(message.channel, "<@%s>, " % (message.author.id), embed=embed)
                            os.remove("no_ping.rtl")

                if message.content.startswith('M 시간'):
                    now = datetime.datetime.now()
                    if now.hour > 12:
                        embed = discord.Embed(title="현재 서버 시간은 %s년 %s월 %s일 오후 %s시 %s분 %s초 입니다!" % (now.year, now.month, now.day, now.hour - 12, now.minute, now.second), description=None, color=Setting.embed_color)
                        embed.set_footer(text = "Seoul. (GMT +09:00) | Ver. %s | %s" % (Setting.version, Copyright))
                        await app.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(title="현재 서버 시간은 %s년 %s월 %s일 오전 %s시 %s분 %s초 입니다!" % (now.year, now.month, now.day, now.hour, now.minute, now.second), description=None, color=Setting.embed_color)
                        embed.set_footer(text = "Seoul. (GMT +09:00) | Ver. %s | %s" % (Setting.version, Copyright))
                        await app.send_message(message.channel, embed=embed)

access_token = os.environ["BOT_TOKEN"]
app.run(access_toekn)
