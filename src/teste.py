-201902 - BD 2B NOITE
Próximas tarefas
Nenhuma tarefa para a próxima semana!
Visualizar tudo

Compartilhe algo com sua turma…
Tarefa: "Atividade contínua 04"
sync4edu Foreducation EdTech postou uma nova tarefa pelo sync4edu: Atividade contínua 04
Criado em: 19:0019:00

Aviso: "Aula 06"
Alex Lopes de Oliveira
Criado em: 19:0019:00
Aula 06

DevOps_aula6.pdf
PDF

jogovelha.txt
Texto

testes.txt
Texto

Aviso: "Prezados alunos, conforme solicitação…"
Alex Lopes de Oliveira
Criado em: 6 de set6 de set
Prezados alunos,
conforme solicitação do Representante de Sala a AC 03 que seria aplicada hoje foi adiada para o dia 13/09. Lembrando que ela abrange o conteúdo das aulas 03 e 04.
Att
Prof. Alex

Aviso: "Aula 05"
Alex Lopes de Oliveira
Criado em: 6 de set6 de set Editado às 6 de set
Aula 05

DevOps_aula5_ProfAlex.pdf
PDF

DevOps_aula05_Alex_1.avi
Vídeo

Aviso: "Aula 04"
Alex Lopes de Oliveira
Criado em: 30 de ago30 de ago Editado às 30 de ago
Aula 04

DevOps_aula4_ProfAlex.pdf
PDF

DevOps_aula04_Alex_1.avi
Vídeo
Tarefa: "Atividade contínua 02"
sync4edu Foreducation EdTech postou uma nova tarefa pelo sync4edu: Atividade contínua 02
Criado em: 30 de ago30 de ago
Tarefa: "Atividade contínua 01"
Alex Lopes de Oliveira postou uma nova tarefa pelo sync4edu: Atividade contínua 01
Criado em: 23 de ago23 de ago Editado às 23 de ago

Aviso: "Aula 03"
Alex Lopes de Oliveira
Criado em: 23 de ago23 de ago Editado às 23 de ago
Aula 03

DevOps_aula3_ProfAlex.pdf
PDF

DevOps_aula03_Alex_1.avi
Vídeo

DevOps_aula03_Alex_2.avi
Vídeo

Aviso: "O AWSome Day Brasil - Conferência…"
Alex Lopes de Oliveira
Criado em: 20 de ago20 de ago
O AWSome Day Brasil - Conferência Online é um evento de treinamento gratuito que fornecerá uma introdução passo-a-passo aos principais serviços da AWS. Nossos especialistas explicarão as características-chave de cada produto e seus diferentes casos de uso, compartilharão as melhores práticas, realizarão demonstrações técnicas e estarão disponíveis para responder suas perguntas.

AWSome Day Brasil
https://pages.awscloud.com/LATAM_TRAINCERT_T2_awsome-day-brasil_20190828_registration-page.html

Aviso: "Aula 02"
Alex Lopes de Oliveira
Criado em: 16 de ago16 de ago Editado às 16 de ago
Aula 02

DevOps_aula2_ProfAlex.pdf
PDF

DevOps_aula02_Alex_1.avi
Vídeo

DevOps_aula02_Alex_2.avi
Vídeo

Aviso: "Aula 01"
Alex Lopes de Oliveira
Criado em: 9 de ago9 de ago
Aula 01

DevOps_aula01_Alex_1.avi
Vídeo

DevOps_aula01_Alex_2.avi
Vídeo

DevOps_aula1_ProfAlex.pdf
PDF

Aviso: "Vaga em DevOps"
Alex Lopes de Oliveira
Criado em: 9 de ago9 de ago
Vaga em DevOps

IMG_20190806_175505604.jpg
Imagem

import jogovelha
import sys

erroInicializar = False


jogo = jogovelha.inicializar()

if len(jogo) != 3:
	erroInicializar = True
else:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroInicializar = True
if erroInicializar:
	sys.exit(1)
else:
	sys.exit(0)