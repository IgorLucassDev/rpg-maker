# RPG Maker - Gerador de Fichas de Personagem

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Um gerador de fichas de personagens para RPG (Role-Playing Game) desenvolvido em Python com interface gráfica Tkinter. Crie personagens aleatórios completos para suas aventuras de Dungeons & Dragons ou outros sistemas de RPG.

## ✨ Funcionalidades

- ✅ **Geração aleatória completa de personagens**
- ✅ **Nome e sobrenome aleatórios** de uma lista extensa
- ✅ **Histórias de fundo** variadas e imersivas
- ✅ **Raças diversificadas** (Anão, Elfo, Humano, Draconato, etc.)
- ✅ **Classes populares** (Guerreiro, Mago, Ladino, Clérigo, etc.)
- ✅ **Tendências alinhadas** (Leal Bom, Caótico Neutro, etc.)
- ✅ **Atributos gerados aleatoriamente** (1-18 para cada atributo)
- ✅ **Idiomas adicionais** além do Comum
- ✅ **Interface amigável** com botão de regeneração

## 🚀 Como Usar

### Pré-requisitos
- Python 3.6 ou superior
- Tkinter (geralmente incluído na instalação padrão do Python)

### Instalação e Execução

1. **Clone ou baixe o projeto:**
```bash
git clone https://github.com/IgorLucassDev/rpg-maker.git
cd rpg-maker
```

2. **Execute o programa:**
```bash
python ./main/gui.py
```

3. **Interface:**
   - Clique em **"Gerar Personagem"** para criar um novo personagem
   - Clique em **"Gerar novamente"** para criar outro personagem aleatório

## 📋 Estrutura do Personagem Gerado

Cada personagem gerado inclui:

- **Nome Completo:** Nome + Sobrenome aleatórios
- **História de Fundo:** Uma das 9 histórias pré-definidas
- **Raça:** Entre 17 opções diferentes
- **Classe:** Entre 12 classes populares
- **Tendência:** Alinhamento moral e ético (9 opções)
- **Atributos:** 
  - Força
  - Destreza
  - Constituição
  - Inteligência
  - Sabedoria
  - Carisma
- **Idiomas:** Comum + um idioma adicional

## 🎮 Exemplo de Saída

```
Nome: Valhein Lulo
História: Este personagem é um ser que cresceu na montanha, trabalhando nas minas 
          de sua família. Ele decidiu se aventurar pelo mundo para encontrar novas 
          riquezas e aventuras, mas também para honrar a memória de seus ancestrais.
Raça: Anão da Montanha
Classe: Guerreiro
Tendência: Neutro Bom
Atributos:
Força: 15 | Destreza: 12 | Constituição: 17
Inteligencia: 10 | Sabedoria: 14 | Carisma: 8

Deslocamento: Padrão (Varia de acordo com o personagem)

Idiomas: Comum Anão
```

## 🛠️ Personalização

### Adicionando mais opções:

1. **Para adicionar novos nomes:**
```python
nome.append('NovoNome')
```

2. **Para adicionar novas histórias:**
```python
historias.append("Sua nova história aqui")
```

3. **Para adicionar novas raças/classes:**
```python
raça.append('Nova Raça')
classe.append('Nova Classe')
```


## 🔧 Possíveis Melhorias Futuras

- [ ] Salvar fichas em arquivo (PDF/TXT)
- [ ] Sistema de pontos para distribuição manual de atributos
- [ ] Adicionar equipamentos iniciais
- [ ] Implementar habilidades de classe específicas
- [ ] Adicionar imagens/avatars para os personagens
- [ ] Suporte a múltiplos sistemas de RPG
- [ ] Exportação para formatos de ficha online

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🎲 Sistemas RPG Compatíveis

- Dungeons & Dragons 5e
- Pathfinder
- Outros sistemas baseados em d20
- Sistemas caseiros com atributos similares

## ✨ Dica para Mestres de RPG

Use este gerador para:
- Criar NPCs (Personagens Não-Jogadores) rapidamente
- Gerar inspiração para personagens de jogadores indecisos
- Criar uma variedade de personagens para encontros aleatórios
- Desenvolver o lore do seu mundo com histórias interessantes

---

**Divirta-se criando heróis (ou vilões) para suas aventuras épicas!** 🐉⚔️🛡️

*Desenvolvido com ❤️ para a comunidade RPG*
