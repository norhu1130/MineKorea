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
                
                if "--" in message.content:
                    if message.author.id == Setting.owner_id:
                        # DPNK 사용 구문 시점
                        embed=discord.Embed(title="루탑봇 전체공지 시스템", color=Setting.embed_color)
                        embed.add_field(name="공지 발신을 준비하고 있습니다!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        embed.set_footer(text = "Module by. Mary | Ver. %s | %s" % (Setting.version, Copyright))
                        mssg = await app.send_message(message.channel, embed=embed)
                        a = []
                        b = []
                        e = []
                        ec = {}
                        embed=discord.Embed(title="루탑봇 전체공지 시스템", color=Setting.embed_color)
                        embed.add_field(name="공지 발신중 입니다!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        embed.set_footer(text = "Module by. Mary | Ver. %s | %s" % (Setting.version, Copyright))
                        await app.edit_message(mssg, embed=embed)
                        for server in app.servers:
                            for channel in server.channels:
                                for tag in ["notice", "공지", "알림", "Alarm"]:
                                    if tag in channel.name:
                                        dtat = True
                                        for distag in ["밴", "경고", "제재", "길드", "ban", "worry", "warn", "guild"]:
                                            if distag in channel.name:
                                                dtat = False
                                        if dtat:
                                            if not server.id in a:
                                                try:
                                                    await app.send_message(channel, message.content)
                                                except discord.HTTPException:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "HTTPException"
                                                except discord.Forbidden:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "Forbidden"
                                                except discord.NotFound:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "NotFound"
                                                except discord.InvalidArgument:
                                                    e.append(str(channel.id))
                                                    ec[channel.id] = "InvalidArgument"
                                                else:
                                                    a.append(str(server.id))
                                                    b.append(str(channel.id))
                        asdf = "```\n"
                        for server in app.servers:
                            if not server.id in a:
                                try:
                                    ch = await app.create_channel(server, "Team-화공-공지-자동생성됨")
                                    await app.send_message(ch, "**__공지 채널을 발견하지 못하여 자동적으로 해당 채널을 생성하였습니다.__**\n자세한 사항은 루탑봇 지원 서버나 팀장 DM으로 부탁드립니다.\n\n지원 서버 : https://invite.gg/rutapbot\nDiscord : HwaHyang - Official#8283")
                                    await app.send_message(ch, message.content)
                                except:
                                    asdf = asdf + str(server.name) + "[채널 생성에 실패하였습니다. (서버 관리자와 연락 요망)]\n"
                                else:
                                    asdf = asdf + str(server.name) + "[채널 생성 및 재발송에 성공하였습니다.]\n"
                        asdf = asdf + "```"
                        embed=discord.Embed(title="루탑봇 전체공지 시스템", color=Setting.embed_color)
                        embed.add_field(name="공지 발신이 완료되었습니다!", value="요청자 : <@" + message.author.id + ">", inline=True)
                        bs = "```\n"
                        es = "```\n"
                        for bf in b:
                            bn = app.get_channel(bf).name
                            bs = bs + str(bn) + "\n"
                        for ef in e:
                            en = app.get_channel(ef).name
                            es = es + str(app.get_channel(ef).server.name) + "(#" + str(en) + ") : " + ec[ef] + "\n"
                        bs = bs + "```"
                        es = es + "```"
                        if bs == "``````":
                            bs = "``` ```"
                        if es == "``````":
                            es = "``` ```"
                        if asdf == "``````":
                            asdf = "``` ```"
                        sucess = bs
                        missing = es
                        notfound = asdf
                        embed.add_field(name="공지 발신에 성공한 채널은 다음과 같습니다 :", value=sucess, inline=False)
                        embed.add_field(name="공지 발신에 실패한 채널은 다음과 같습니다 :", value=missing, inline=False)
                        embed.add_field(name="키워드가 발견되지 않은 서버는 다음과 같습니다 :", value=notfound, inline=False)
                        embed.set_footer(text = "Module by. Mary | Ver. %s | %s" % (Setting.version, Copyright))
                        await app.edit_message(mssg, embed=embed)
                        # DPNK 사용 구문 종점
                        log_actvity("I send Notice for all Server. (content : %s\nSuccess : %s\nFail : %s\nNotfound : %s)." % (message.content, sucess, missing, notfound))
                    else:
                        await app.send_message(message.channel, "<@%s>, 봇 관리자로 등록되어 있지 않습니다. `setting.py` 파일을 확인하여 주세요." % (message.author.id))

                
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
                  embed.add_field(name='Raeto0322Bot', value='https://github.com/haveadooday/Raeto0322Bot-')
                  await app.send_message(message.channel, embed=embed) 

                if message.content.startswith('-봇프사'):
                  embed=discord.Embed(title='Bot profile photo', description=None, color=0x00ff00)
                  embed.add_field(name='Bot Profile', value='봇의 프로필 사진입니다.')
                  await app.send_message(message.channel, embed=embed)
                  await app.send_message(message.channel, "https://cdn.discordapp.com/attachments/558971678583947264/559186971587510284/image0.png")

                if message.content.startswith("-마크사이트"):
                  embed=discord.Embed(title='Mojang 사이트', description=None, color=0x00ff00)
                  embed.add_field(name='https://minecraft.net/ko-kr/?ref=m', value='마인크래프트 사이트입니다.')
                  await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-하이픽셀'):
                  embed=discord.Embed(title='Hypixel Network', desription=None, color=0x00ff00)
                  embed.add_field(name='MC.hypixel.net', value='하이픽셀은 개발자도 많이 겜하는 서버!')
                  await app.send_message(message.channel, embed=embed) 

                if message.content.startswith("-온라인"):
                  embed=discord.Embed(title='온라인 상태', description=None, color=0x00ff00)
                  embed.add_field(name='I am online!', value='현재 온라인 상태입니다.')
                  await app.send_message(message.channel, embed=embed)  

                if message.content.startswith('-도움말'):
                   embed=discord.Embed(title="AmoBot 도움말입니다.기본 접두사는 `-`입니다.", description=None, color=0x00ff00)
                   embed.add_field(name='-봇프사', value='봇의 프로필 정보를 출력합니다. '  )
                   embed.add_field(name='-사용소스', value='봇의 사용된 소스를 출력합니다. '  )
                   embed.add_field(name='-마크사이트', value='마인크래프트 공식 사이트를 출력합니다.')
                   embed.add_field(name='-온라인', value='봇이 온라인인지 확인합니다.메세지가 출력이 되지 않을 경우 오프라인입니다.')
                   embed.add_field(name='-정보', value='봇의 정보를 출력합니다.')
                   embed.add_field(name='-도움말', value='명령어 전체를 출력합니다.')
                   embed.add_field(name='-개발프로그램', value='개발 프로그램을 출력합니다.')
                   embed.add_field(name='-아이디', value='당신의 유저아이디를 출력합니다.')
                   embed.add_field(name='-개발자 정보', value='개발자 정보를 출력합니다.')
                   await app.send_message(message.author, embed=embed)

                if message.content.startswith('-개발프로그램'):
                   embed=discord.Embed(title='개발 프로그램 내역입니다.', description=None, color=0x00ff00)
                   embed.add_field(name='언어', value='Python 3.5.4')
                   embed.add_field(name='소스 수정 프로그램', value='Visual Studio Code')
                   await app.send_message(message.channel, embed=embed)  

                if message.content.startswith('-개발자명령어'):
                   if message.author.id == Setting.owner_id:
                    embed=discord.Embed(title="Only admin command!")
                    embed.add_field(name='--공지', value='아직 공개 되지 않은 것')  
                    embed.add_field(name='--공지설정', value='공지 내용을 등록합니다.')
                    embed.add_field(name='--공지발신', value='공지 내용을 발신합니다.')
                    embed.add_field(name='--종료', value='봇을 종료합니다.')  
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-아이디'):
                   embed=discord.Embed(title="당신의 유저 아이디 입니다.", color=0x00ff00)
                   embed.add_field(name=str(message.author.id), value='요청자 : ' + "<@" + str(message.author.id) + ">")
                   await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-개발자 정보'):
                   embed=discord.Embed(title='개발자 정보', description=None, color=0x00ff00)
                   embed.add_field(name='MineAmo Computer #4899', value='총개발자')
                   await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-정보'):
                    embed = discord.Embed(title="AmoBot 정보!", description=None, color=0x00ff00)
                    embed.add_field(name="[Amo Bot 홈페이지]", value="https://minekorea.modoo.at/", inline=False)
                    embed.add_field(name="[Amo Bot 개발자]", value="-개발자 정보", inline=False)
                    embed.add_field(name="[오픈소스 사용]", value="-사용소스", inline=False)
                    embed.add_field(name="[Amo Bot 공식 링크]", value="https://discord.gg/hdHPjUA", inline=False)
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-사용서버'):
                   await app.send_message(message.channel, "사용된서버 %s" % (len(app.servers)))

                if "-서버정보" == message.content:
                    embed = discord.Embed(title="\"%s\" 서버정보!" % (message.server.name), description=None, color=Setting.embed_color)
                    embed.add_field(name="서버 소유자", value="<@%s>" % message.server.owner.id, inline=False)
                    embed.add_field(name="서버 생성일", value="%s (UTC)" % (message.server.created_at), inline=False)
                    embed.add_field(name="서버 보안등급", value=message.server.verification_level, inline=False)
                    embed.add_field(name="서버 위치", value=message.server.region, inline=False)
                    embed.add_field(name="서버 잠수채널", value="%s (%s분 이상 잠수이면 이동됨)" % (message.server.afk_channel, message.server.afk_timeout/60), inline=False)
                    embed.set_thumbnail(url=message.server.icon_url)
                    embed.set_footer(text = "Server ID : %s | Ver. %s | %s" % (message.server.id, Setting.version, Copyright))
                    await app.send_message(message.channel, embed=embed)

                if message.content.startswith('-시간'):
                    now = datetime.datetime.now()
                    if now.hour > 12:
                        embed = discord.Embed(title="현재 서버 시간은 %s년 %s월 %s일 오후 %s시 %s분 %s초 입니다!" % (now.year, now.month, now.day, now.hour - 12, now.minute, now.second), description=None, color=Setting.embed_color)
                        embed.set_footer(text = "Seoul. (GMT +09:00) | Ver. %s | %s" % (Setting.version, Copyright))
                        await app.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(title="현재 서버 시간은 %s년 %s월 %s일 오전 %s시 %s분 %s초 입니다!" % (now.year, now.month, now.day, now.hour, now.minute, now.second), description=None, color=Setting.embed_color)
                        embed.set_footer(text = "Seoul. (GMT +09:00) | Ver. %s | %s" % (Setting.version, Copyright))
                        await app.send_message(message.channel, embed=embed)
                                    
                if message.content.startswith('-문의'):
                      learn = message.content.replace('-문의', "")
                      embed = discord.Embed(title='문의전송안내',description='문의내용:'+learn+'\n 혹시 잘못전송되었으면 다시문의를 하여 "취소합니다."',color=0x00ff00)
                      await client.send_message(channel,embed=embed)
                      a = learn[1]
                      file = open('문의채널.txt')
                      channel1 = discord.Object(id=file.read())
                      file.close()
                      embed = discord.Embed(title='문의 수신',description='문의전송안내'+'아이디:'+id+'이름:'+message.author.name+'\n 내용:'+learn,color=0x00ff00)
                      await app.send_message(channel1,embed=embed)
                   
                if message.content.startswith('-답변'):
                    learn = message.content.split(' ')
                    embed = discord.Embed(title='문의답변',description='답변이 왔습니다. \n 내용:'+learn[2],color=0x00ff00)
                    member = discord.utils.get(client.get_all_members(),id=learn[1])
                    await client.send_message(member,embed=embed)
                    await client.send_message(channel,':white_check_mark:')

                   

access_token = os.environ["BOT_TOKEN"]
app.run(access_toekn)
