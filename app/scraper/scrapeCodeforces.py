import requests as req

URL = "https://codeforces.com/api/contest.list"

def convert(seconds):
    seconds = seconds % (24 * 3600)
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    return [days, hours]

def fetchCodeforces(url=URL):
    response = req.get(url)
    contests = response.json()['result']
    # filter through the contests and take only the ones that are not over yet
    
    if response.status_code != 200:
        return []
    else:
        upcoming_contests = []
        for contest in contests:
            if contest['phase'] == 'BEFORE':
                #get the contest name, start time in days and hours fconvert it from seconds to days and hours and id
                contest_name = contest['name']
                start_time = convert(contest['startTimeSeconds'])
                duration = contest['durationSeconds']
                contest_id = contest['id']

                contest_info = [
                    contest_id,
                    contest_name,
                    start_time,
                    duration
                ]
                upcoming_contests.append(contest_info)
            else:
                break
        return upcoming_contests