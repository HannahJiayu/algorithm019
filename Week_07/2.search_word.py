
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        END_OF_WORD = "#"
        trie = {}
        res = set()
        if not board or not board[0] or not words:
            return []
        
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[END_OF_WORD] = END_OF_WORD
    
        def _dfs(row, col, cur_word, parent):
            letter = board[row][col]
            cur_node = parent[letter]
            cur_word = cur_word + letter
            board[row][col] = '$'
            if END_OF_WORD in cur_node:
                res.add(cur_word)

            for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                _row, _col = row + i, col + j
                if 0 <= _row < len(board) and 0 <= _col < len(board[0]) and board[_row][_col] != '$' and board[_row][_col] in cur_node.keys():
                    _dfs(_row, _col, cur_word, cur_node)
            board[row][col] = letter
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.keys():
                    _dfs(i, j, '', trie)
        return list(res)


            