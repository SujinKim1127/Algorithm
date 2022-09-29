/**
 * 문자열을 입력받아 해당 문자열에 등장하는 두 칸의 공백을 모두
 * 한 칸의 공백으로 바꾼 문자열을 리턴
 */

function convertDoubleSpaceToSingle(str) {
    // 먼저 split으로 잘라주고
    var words = str.split("  ")
    // 자른걸 한칸으로 합해준다
    return words.join(" ")
  }
  