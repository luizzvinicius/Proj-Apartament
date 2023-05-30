import statistics

def notas(*pontuacao, sit=False):
    info = {
        "total": len(pontuacao), 
        "media": statistics.mean(pontuacao), 
        "Maior nota": max(pontuacao), 
        "Menor nota": min(pontuacao)
    }
    
    situacao = ""
    if sit:
        if info["media"] > 6:
            situacao = "Boa"
            info["Situacao"] = situacao
        else:
            situacao = "Ruim"

    return info

print(notas(3, 9, 9, 7, 9, sit=True))
print(notas(1, 5, 10, 7, 5.5))
