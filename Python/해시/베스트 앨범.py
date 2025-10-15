def solution(genres, plays):
    answer = []
    hashmap = {}
    total = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in hashmap:
            hashmap[genre] = []
            total[genre] = 0
        hashmap[genre].append((play, i))
        total[genre] += play
    
    print("t", total)
    genres_by_total = sorted(total.items(), key=lambda x: -x[1])
    print(genres_by_total)
    for g,_ in genres_by_total:     # total 큰 값부터 
        songs = hashmap[g]
        songs.sort(key=lambda x: (-x[0], x[1]))     # (3번 조건) 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
        print("songs", songs)
        answer.extend(idx for _, idx in songs[:2])

    return answer