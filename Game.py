import newEleusisPlayer
def main():
    god_rule = "iff(is_royal(current),True)"
    board = [('QS',[]),('KC',[]),('JH',[])]
    player = newEleusisPlayer.Player(board, god_rule)
    predicted_rule = player.scientist()
    print(predicted_rule)


if __name__ == "__main__":
    main()