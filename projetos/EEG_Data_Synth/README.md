# Estudo de Caso: Síntese de Dados de EEG utilizando Redes Generativas Adversárias
# Case Study: EEG Data Synthesis through Generative Adversarial Networks

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de pós-graduação *IA376L - Deep Learning aplicado a Síntese de Sinais*, 
oferecida no segundo semestre de 2023, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).

|Nome  | RA | Especialização|
|--|--|--|
| Joany Rodrigues  | 264440  | Eng. de Computação|
| João Guilherme Prado Barbon  | 262760  | Eng. Físico|
| Larissa Rangel de Azevedo  | 247008  | Eng. Eletricista|

## Apresentação Final
[Link](https://docs.google.com/presentation/d/1Imx5d8NEQsX_pNUUmQK9wvczdD66szTr/edit?usp=sharing&ouid=106498812395082097833&rtpof=true&sd=true) para apresentação final.

## Descrição Resumida do Projeto
<!-- Este projeto tem como objetivo sintetizar dados de eletroencefalografia (EEG) gerados por uma interface cérebro-computador (BCI) utilizando o paradigma de imagética motora. A principal motivação da implementação de uma BCI é o estudo e a compreensão do cérebro, abrindo portas para aplicações na área da saúde e entretenimento. A abordagem do paradigma da imagética motora ocorre pela aquisição dos sinais cerebrais gerados pela imaginação ou realização do movimento de partes do corpo, como membros superiores (braços) ou inferiores (pernas). Assim, os dados sintéticos serão gerados a partir de uma Rede Generativa Adversária (GAN), que apresentará como saída séries temporais representativas dos sinais reais de EEG.  
 -->
Este projeto tem como objetivo sintetizar dados de eletroencefalografia (EEG) gerados por uma interface cérebro-computador (BCI, do inglês Brain-Computer Interface) utilizando o paradigma de imagética motora. Esse sistema apresenta um vasto potencial para aplicações inovadoras, com benefícios notáveis, sobretudo considerando a população que enfrenta diversos tipos de deficiências (sejam elas visuais, auditivas, motoras ou cognitivas), bem como o crescente mercado das tecnologias assistivas e interativas. A principal motivação subjacente à implementação das BCIs é o estudo e a compreensão do funcionamento cerebral, abrindo caminhos para aplicações nos campos da saúde e entretenimento. 

Uma abordagem notável dentro desse contexto é a utilização do paradigma de imagética motora, que envolve a aquisição de sinais cerebrais gerados pela imaginação ou execução de movimentos de partes do corpo, como membros superiores (braços) e inferiores (pernas). Buscando uma melhor reprodutibilidades desses sinais, a geração de dados sintéticos será realizada por meio de uma Rede Generativa Adversária (GAN), que produzirá séries temporais dos sinais de EEG reais. Tal abordagem oferece a capacidade de criar conjuntos de dados EEG diversificados e representativos, que podem ser usados para desenvolver e aprimorar sistemas BCI de classificação, tornando-os mais precisos e eficazes e abrangendo uma ampla variedade de cenários e condições. 

[Vídeo da Apresentação - 1ª entrega ](https://drive.google.com/file/d/1T1XJYjW1v4Qm5PvELuSoJu00xOpP94OW/view)

## Metodologia Proposta
- A base de dados que será utilizada é a [BNCI2014_001](https://moabb.neurotechx.com/docs/generated/moabb.datasets.BNCI2014_001.html#r55ebd47d0fe7-1), que consiste em dados de EEG de nove indivíduos, com quatro classes de movimento diferentes: movimento da mão esquerda (classe 1), da mão direita (classe 2), de ambos os pés (classe 3) e da lingua (classe 4). Este dataset foi utilizado no Review BCI Competition 4, sendo portanto bem documentado e testado.
- Como principal modelo generativo, serão utilizadas GANs para geração dos dados sintéticos. Como abordagem, utilizamos uma Conditional DCGAN, inspirada no artigo [EEG-GAN](https://arxiv.org/abs/1806.01875).
- Outro artigo de referência utilizado analisa o impacto do aumento de dados sintéticos de EEG na avaliação de classificadores - [Augmenting EEG with Generative Adversarial Networks Enhances Brain Decoding Across Classifiers and Sample Sizes](https://escholarship.org/uc/item/9gz8g908)
-  As ferramentas utilizadas serão:
    - Linguagem:  Python
    - Biblioteca: Pythorch
    - Ambiente: Google Colab e Kaggle
  
- Os resultados esperados são distribuições de dados sintéticos de EEG que melhor se aproximam das distribuições reais. Para verificar se as distribuições são compatíveis, mapeou-se os dados para um manifold de menor dimensão utilizando Variational Autoencoder. Como métricas de avaliação, utilizou-se a divergência de Jensen–Shannon, a acurácia do classificador EEGNet e histogramas da distribuição estatística dos dados.
### Bases de Dados e Evolução

|Base de Dados | Endereço na Web | Resumo descritivo|
|----- | ----- | -----|
|BNCI2014_001| https://encurtador.com.br/lpsAK| Dados de EEG de 9 indivíduos, adquiridos por meio 22 eletrodos dispostos no escalpo de cada indivíduo, durante o experimento de realização de 4 movimentos diferentes. 

<!---

> Faça uma descrição sobre o que concluiu sobre esta base. Sugere-se que respondam perguntas ou forneçam informações indicadas a seguir:
>
> 
> * Qual o formato dessa base, tamanho, tipo de anotação? 
-->

 A base de dados utilizada possui formato "braindecode.datasets.moabb.MOABBDataset", que é o formato padrão da toolboox Braindecode.  O [Braindecode](https://braindecode.org/stable/index.html) é uma biblioteca open-source em Python usada decodificar dados brutos de EEG, ECoG e MEG, contendo funções como dataset fetchers, ferramentas de pré-processamento e visualização de dados, além de algumas arquiteturas de aprendizado profundo.

 Em seu formato original, para apenas um indivíduo, a base possui 12 runs, sendo seis runs de treinamento e seis de validação. Uma run contém dados de EEG totalizando 6:27 minutos, coletados através de 22 eletrodos com frequências entre 0 Hz e 125 Hz, e amostragem de 250 Hz (ou seja, 250 amostras por segundo). No formato tensorial, uma run pode ser descrita como uma matriz de (96750 x 22), onde as linhas são as medições e as colunas os respectivos eletrodos.

<!---
> * Quais as transformações e tratamentos feitos? Limpeza, reanotação, etc.
your comment goes here
and here
-->

As transformações foram feitas usando a biblioteca 'braindecode.preprocessing.Preprocessor', que  aplica a função de pré-processamento fornecida aos dados brutos. 
A primeira transformação realizada foi uma reamostragem para 100 Hz e uma filtragem utilizando um filtro passa faixas com frequências de corte de 4 e 38 Hz, para eliminar frequências irrelevantes, por exemplo  60 Hz oriunda da rede elétrica. Além disso, foi utilizado um filtro CAR - [Common Average Reference](https://pressrelease.brainproducts.com/referencing/#:~:text=When%20applying%20the%20so%2Dcalled,resulting%20signal%20from%20each%20channel.) - para remover os ruídos internos e externos, e os dados normalizados utilizando [Starndard Scale](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html). 

Por último, foi feito o janelamento dos dados em janelas de  4s (400 amostras) para dividir os dados entre as 4 classes e reduzir a quantidade de amostras processadas pelo o algoritmo, melhorando também o tempo de processamento. Neste processamento, todos os 22 eletrodos foram utilizados. A Figura 1 abaixo mostra um exemplo de sinal de EEG no domínio da frequência para todos os eletrodos.

|![EEG Channels Frequency Curve](./figure/eeg_frequency_example.png "EEG Channels Frequency Curve")Figura 1: Espectro de EEG para todos os 22 eletrodos. Fonte: Própria. |
|:--:| 

A Tabela 1 a seguir mostra como estão dispostos os para um dos sujeitos da base de dados, Q1, median e Q3 são respectivamente o primeiro quartil, a mediana e o terceiro quartil, que representam as estatísticas descritivas da base de dados após o pré-processamento. Na Tabela 2 tem-se em resumo as informações relevantes  usadas no projeto. 

|*Tabela 1: Estatísticas descritivas da base de dados*|
|:--:| 

| ch  | name  | type | unit | min           | Q1          | median  | Q3          | max          |
|----:|-------|------|------|--------------:|------------:|--------:|------------:|------------:|
|   0 | Fz    | EEG  | µV   | -23197412.26  | -2764233.74 | -59893.33 | 2689774.31  | 24117502.14 |
|   1 | FC3   | EEG  | µV   | -16092798.07  | -2262880.58 |  9058.88 | 2221504.87  | 16416656.78 |
|   2 | FC1   | EEG  | µV   | -19583299.93  | -2197222.31 | -3899.04 | 2155626.09  | 16767533.19 |
|   3 | FCz   | EEG  | µV   | -20189703.99  | -2348475.26 | -34185.20 | 2288364.73  | 17884609.01 |
|   4 | FC2   | EEG  | µV   | -16651394.00  | -2096426.26 | -17829.59 | 2072305.99  | 17704307.52 |
|   5 | FC4   | EEG  | µV   | -17091787.21  | -2257461.58 | -16192.81 | 2252035.06  | 17556741.76 |
|   6 | C5    | EEG  | µV   | -16363957.84  | -2464807.19 |  28147.23 | 2456031.64  | 21078452.11 |
|   7 | C3    | EEG  | µV   | -21211591.44  | -1746918.71 |  33566.48 | 1796777.18  | 21687721.12 |
|   8 | C1    | EEG  | µV   | -23428939.98  | -1387423.47 |  11196.68 | 1404395.06  | 30463036.86 |
|   9 | Cz    | EEG  | µV   | -14918655.42  | -1643685.54 |  -6336.32 | 1638304.56  | 14533799.88 |
|  10 | C2    | EEG  | µV   | -10423506.98  | -1388777.30 |   3095.53 | 1406398.20  | 10402446.50 |
|  11 | C4    | EEG  | µV   | -17684305.36  | -1813621.59 |  17419.43 | 1840669.03  | 12688415.45 |
|  12 | C6    | EEG  | µV   | -21559642.80  | -2631099.24 | -12882.52 | 2641556.70  | 23328653.66 |
|  13 | CP3   | EEG  | µV   | -17972880.92  | -2152442.25 | 61684.71 | 2240892.25  | 15908321.92 |
|  14 | CP1   | EEG  | µV   | -14620068.46  | -1444056.81 | 37891.09 | 1482102.75  | 18123839.36 |
|  15 | CPz   | EEG  | µV   | -13303892.60  | -1416615.66 |   762.69 | 1422849.62  | 12948253.60 |
|  16 | CP2   | EEG  | µV   | -11823591.95  | -1329206.34 | 16067.51 | 1362674.56  | 10213997.18 |
|  17 | CP4   | EEG  | µV   | -25137329.68  | -2018397.32 | 34057.89 | 2061892.99  | 16786867.70 |
|  18 | P1    | EEG  | µV   | -19384165.37  | -2311265.52 | 55445.33 | 2338381.92  | 19757396.00 |
|  19 | Pz    | EEG  | µV   | -24524615.78  | -2097203.73 | 20822.05 | 2128965.70  | 15253330.64 |
|  20 | P2    | EEG  | µV   | -30192611.43  | -2272931.93 |   255.07 | 2316270.46  | 18435264.58 |
|  21 | POz   | EEG  | µV   | -36473536.55  | -3385989.48 | -12468.79 | 3385965.87  | 29828793.42 |


|*Tabela 2: Aspectos principais da base usados no projeto.*|
|:--:| 

Informações  | Descrição
--------- | ------
Eletrodos | 'Fz','FC3','FC1','FCz','FC2','FC4','C5','C3','C1','Cz','C2','C4','C6','CP3','CP1','CPz','CP2','CP4','P1','Pz','P2','POz'
Runs | 12
Janelas por Run | 96
Janelas por Classe| 24
Classes | 'feet': 0, 'left_hand': 1, 'right_hand': 2, 'tongue': 3
Tempo por Janela | 4s
Amostras por Janela | 400



## Workflow
Na Figura 2 tem-se o workflow da *Conditional DCGAN* implementada, em que a Rede Generativa contém 4 camadas convolucionais que recebem como entrada um ruído de dimensão (n_amostras,68,1,1) e retorna dados sintéticos de dimensão (n_amostras,1,22,400). A Rede Discriminativa possui 2 camadas convolucionais para classificação dos dados em reais ou falsos e recebe em sua entrada os dados reais pré-processados também com dimensão (n_amostras,1,22,400). Para o esquema da Figura 2, utilizou-se um exemplo de *n_amostras = 4*.

|![Workflow](./figure/new_workflow.jpeg "Workflow")**Figura 2: Workflow da Conditional DCGAN. Fonte: Própria.**|
|:--:| 

O código implementado da arquitetura da DCGAN utilizada neste trabalho pode ser encontrada no [GitHub](https://github.com/jbarbon/dgm-2023.2/blob/main/projetos/EEG_Data_Synth/notebooks/GANs/MyGAN.py).


### Criação de ruído
O ruído para o treinamento do gerador foi criado pela amostragem de dados aleatórios de uma distribuição normal, utilizando a função `torch.randn`. Além do ruído, gerado com dimensão `(n_amostras,64)`, também é criado um tensor de labels no formato one-hot encoding para este sinal, com dimensão `(n_amostras,4)`. Para obter a entrada final do gerador, concatena-se o ruído com as labels dos dado reais, com dimensão `(n_amostras, 68)`. Por fim, é realizada uma conversão para transformar o ruído no formato tensorial dos dados de EEG, `(n_amostras,68,1,1)`.

### Rede generativa
A rede generativa possui quatro camadas convolucionais, que recebe o sinal de ruído de dimensão `(n_amostras,68,1,1)` e gera um sinal falso de EEG de dimensão `(n_amostras,1,22,400)`. As três primeiras camadas realizam as operações:

```python
nn.ConvTranspose2d(64, 256, kernel_size = (3,60), stride = (1,1)),
nn.BatchNorm2d(272),
nn.ReLU(inplace=True),

nn.ConvTranspose2d(256, 128, kernel_size = (4,60), stride = (3,1)),
nn.BatchNorm2d(136),
nn.ReLU(inplace=True),

nn.ConvTranspose2d(128, 64, kernel_size = (3,60), stride = (2,1)),
nn.BatchNorm2d(68),
nn.ReLU(inplace=True),

```

A última camada realiza uma convolução transposta acompanhada de uma função de ativação Tanh:

```python
    nn.ConvTranspose2d(64, 1, kernel_size = (2,50), stride = (1,2), padding = (0,2)),
    nn.Tanh()
```

### Rede discriminativa
A rede discriminativa classifica os dados de entrada como reais ou falsos. Ela recebe como entrada um tensor do sinal de EEG concatenado com os labels de cada amostra, produzindo um tensor de dimensão `(n_amostras,5,22,400)`. Esta rede possui três camadas convolucionais que realizam as seguintes operações:

```python
    # Layer 1
    nn.Conv2d(5, 64,   kernel_size = (4,50), stride = (3,4)),
    nn.BatchNorm2d(64),
    nn.LeakyReLU(0.2, inplace=True)

    # Layer 2
    nn.Conv2d(64, 128,  kernel_size = (3,50), stride = (2,4)),
    nn.BatchNorm2d(128),
    nn.LeakyReLU(0.2, inplace=True)

    # Layer 3
    nn.Conv2d(128, 1,  kernel_size = (3,10), stride = (1,1)),

```

### Configuração de treinamento da DCGAN

O treinamento da DCGAN foi feito com os dados EEG do indivíduo 3 do dataset, utilizando todas as 12 runs (treino + validação). Todos os eletrodos foram selecionados e as classes `'feet': 0, 'left_hand': 1, 'right_hand': 2, 'tongue': 3` de cada amostra foi transformada no formato one-hot encoding para posterior concatenação com o ruído de entrada no gerador e com os dados da entrada do classificador.

As configurações de treinamento da rede e o algoritmo de treinamento são mostrados a seguir:

| Parâmetros | Valor | 
|:---------:|:-----:|
|Número de épocas|200|
|Dimensão do ruído|64|
|Tamanho do batch| 64|
|Learning Rate| 3.7e-5|
|Decay Rate| 0.7|
|Loss Function|`nn.BCEWithLogitsLoss`|


### Algoritmo de Treinamento da DCGAN

#### Passo 1: Inicialização
- Para cada época no número total de épocas (n_epochs):
  - Para cada lote de imagens reais e suas labels no conjunto de dados:
    - Converta os dados reais em tensores e mova para o dispositivo de processamento (GPU).

#### Passo 2: Atualizar o Discriminador
- Zere os gradientes do discriminador.
- Gere dados EEG falsos usando o gerador:
  - Combine os vetores de ruído falsos com as labels one-hot correspondentes.
  - Gere os dados EEG falsos condicionados.
- Obtenha as previsões do discriminador para dados falsos e reais:
  - Crie a entrada para o discriminador:
    - Combine as imagens falsas com labels one-hot e desconecte o gerador para não retropropagar.
    - Combine as imagens reais com labels one-hot.
  - Obtenha a previsão do discriminador para os dados falsos.
  - Obtenha a previsão do discriminador para os dados reais.
- Calcule as perdas do discriminador:
  - Calcule a perda para dados falsos usando uma função de perda que compara as previsões com um vetor de zeros.
  - Calcule a perda para dados reais usando a mesma função de perda, comparando as previsões com um vetor de uns.
- Calcule a perda total do discriminador como a média das perdas para dados falsos e reais dividida por dois.
- Realize a retropropagação das perdas e atualize os gradientes do discriminador.
- Armazene a perda média do discriminador na lista de perdas do discriminador.

#### Passo 3: Atualizar o Gerador
- Zere os gradientes do gerador.
- Crie novamente a entrada para o discriminador usando os dados EEG falsos gerados e as labels one-hot.
- Obtenha as previsões do discriminador para os dados EEG falsos gerados.
- Calcule a perda do gerador usando a função de perda que compara as previsões com um vetor de uns (indicando que os dados falsos devem parecer reais).
- Realize a retropropagação da perda e atualize os gradientes do gerador.


## Métricas de avaliação
Nesta seção são explicadas as métricas de avaliação adotadas para verificar a qualidade dos dados sintéticos em comparação com os dados reais. 

### Classificador
Para a comparação das acurácias utilizou-se uma implementação do classificador da [EEGNetV4](https://braindecode.org/stable/generated/braindecode.models.EEGNetv4.html) disponível na biblioteca ``braindecode`` para classificar as labels dos dados de EEG. A estrutura do classificador foi baseada no artigo [EEGNet](https://arxiv.org/abs/1611.08024), e os parâmetros de treinamento utilizados foram os padrões da biblioteca, adaptados aos nossos dados:

```python
n_epochs = 300

model = EEGNetv4(
      in_chans = 22,
      n_classes = 4,
      input_window_samples= 400,
      final_conv_length='auto',
      F1=8,
      D=2,
      F2=8,
      kernel_length=64,
      drop_prob=0.5
)
 ```

Nesta métrica, o objetivo é, inicialmente, treinar o classificador no conjunto completo de dados reais de EEG, obtendo um valor base de acurácia. Após o treinamento da GAN, utiliza-se o gerador para gerar novas amostras que irão compor o conjunto original de dados, processo conhecido como data augmentation. Espera-se, portanto, que o classificador treinado neste novo conjunto de dados (reais + falsos) apresente melhores valores de acurácia, melhorando o processo de classificação dos movimentos para este paradigma cérebro-computador. Foram utilizados diferentes valores de augmentation para comparação da eficiência na classificação: 

   ``0% (base), '5%', '10%', '20%', '50%', '70%', '100%', '200%' ``

### Divergência de Jensen Shannon (JS)
<!-- A divergencia de Jensen Shannon é uma métrica que mede o quanto duas distribuições divergem entre si. É baseado na divergência de Kullback-Leibler, mas é simétrica. Utilizamos a biblioteca scipy para [implementação](https://github.com/jbarbon/dgm-2023.2/tree/main/projetos/EEG_Data_Synth/notebooks/GANs/JS_metric.ipynb). -->

A divergência de Jensen-Shannon é um método para medir a similaridade entre duas distribuições de probabilidade. Ela é baseada na divergência de Kullback-Leibler, com simetria entre as distribuições e sempre com um valor finito. A raiz quadrada da divergência de Jensen-Shannon é referida como a distância de Jensen-Shannon.

A fórmula para calcular a divergência de Jensen-Shannon é uma combinação ponderada das divergências de Kullback-Leibler entre as distribuições de probabilidade de interesse e sua média. Isso resulta em uma medida que captura tanto as semelhanças quanto as diferenças entre as distribuições, tornando-a uma métrica valiosa para tarefas de classificação, clusterização e recuperação de informações. A implementação utilizada neste trabalho pode ser encontrada neste [link](https://github.com/jbarbon/dgm-2023.2/tree/main/projetos/EEG_Data_Synth/notebooks/GANs/JS_metric.ipynb).


### Histogramas

Histogramas foram utilizados para comparação visual entre as distribuições dos canais dos dados reais e dados sintéticos, na proporção de 1:1. Para análise, foram escolhidos três eletrodos posicionados na região motora do cérebro (Cz, C3 e C4) e dois eletrodos cujo valor de divergência de JS mais variaram de indivíduo para indivíduo (FC2, C2). 

### Espaços latentes de um Autoencoder Variacional
A arquitetura de um Autoencoder Variacional (VAE) foi utilizada para gerar o espaço latente dos dados reais e sintéticos através da extração de característica realizada pelo encoder. Após alguns testes e alterações no código original (o código fonte usado está disponível no [GitHub](https://github.com/arkanivasarkar/EEG-Data-Augmentation-using-Variational-Autoencoder)) obteve-se a seguinte configuração final: 

* Modelo do Encoder: 

| Layer (type)                  | Output Shape           | Param #      | Connected to                |
|-------------------------------|------------------------|--------------|-----------------------------|
| encoder_input (InputLayer)    | (None, 1, 22, 400)     | 0            | []                          |
| conv2d (Conv2D)               | (None, 1, 1, 32)       | 640,032      | ['encoder_input[0][0]']     |
| batch_normalization           | (None, 1, 1, 32)       | 128          | ['conv2d[0][0]']            |
| leaky_re_lu                   | (None, 1, 1, 32)       | 0            | ['batch_normalization[0][0]']|
| conv2d_1 (Conv2D)             | (None, 1, 1, 64)       | 45,120       | ['leaky_re_lu[0][0]']       |
| batch_normalization_1         | (None, 1, 1, 64)       | 256          | ['conv2d_1[0][0]']          |
| leaky_re_lu_1                 | (None, 1, 1, 64)       | 0            | ['batch_normalization_1[0][0]']|
| flatten                       | (None, 64)             | 0            | ['leaky_re_lu_1[0][0]']     |
| dense                         | (None, 16)             | 1,040        | ['flatten[0][0]']           |
| z_log_var (Dense)             | (None, 2)              | 34           | ['dense[0][0]']             |
| z_mean (Dense)                | (None, 2)              | 34           | ['dense[0][0]']             |
| tf.math.add (TFOpLambda)      | (None, 2)              | 0            | ['z_log_var[0][0]']         |
| z (Lambda)                    | (None, 2)              | 0            | ['z_mean[0][0]', 'tf.math.add[0][0]']|

Com a arquitetura final do VAE, composta pela junção do codificador e do decodificador, foi possível realizar o treinamento por 1000 épocas, usando um tamanho de lote (batch size) igual a 32 e uma dimensão do espaço latente fixada em 2.

* Modelo do VAE: 

| Layer (type)                | Output Shape         | Param #   |
|-----------------------------|----------------------|-----------|
| encoder_input (InputLayer)  | (None, 1, 22, 400)   | 0         |
| encoder (Functional)        | (None, 2), (None, 2),| 686,644   |
|                             | (None, 2)            |           |
| decoder (Functional)        | (None, 1, 22, 400)   | 910,785   |

* Parâmetros do treinamento: 

| Parâmetro | Valor | 
|:---------:|:-----:|
|Número de épocas|1000|
|Dimensão latente|2|
|Tamanho do batch| 32|
|Otimizador| Adam|
|Learning Rate| 0.001|
|Loss Function|`mse`|

As predições geradas pelo *encoder* foram submetidas ao métodos do [K-means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) para geração dos rótulos das classes, em seguida para a visualização dos manifolds, empregou-se a biblioteca [UMAP](https://umap-learn.readthedocs.io/en/latest/). Como resultado, obteve-se o espaço latente tanto para a base de dados real quanto para a base de dados sintéticos, permitindo a comparação de suas representações por meio dos manifolds em cada cenário. 

# Resultados

## Resultados para o terceiro indivíduo
Nesta seção inicial, apresentam-se os resultados relacionados aos dados de EEG provenientes do indivíduo 3, uma vez que ele foi utilizado como referência para o ajuste fino dos parâmetros. Na próxima seção, será realizada uma comparação dos resultados entre os indivíduos 1, 3, 7 e 9.


### Curvas de Loss da GAN

Ao final do treinamento da GAN, gerou-se um gráfico exibindo as curvas de perda para o gerador e o discriminador em função das épocas, mostrado na [Figura 2](22ch_batch64_lr37e6_decay7.png). A figura ilustra o comportamento observado para a melhor arquitetura e parâmetros encontrados, com o discriminador convergindo para valores de perda muito próximos `0.5`, e o gerador convergindo para valores próximos de `0.8`, ambos resultados desejáveis no treinamento adversário. 

|![Loss Curve](./figure/subject_3/22ch_batch64_lr37e6_decay7.png "Loss Curve")**Figura 3: Convergência da curva de loss do gerador e discriminador**|
|:--:| 

### Classificador
A acurácia do classificador para os dados aumentados são mostrados na tabela abaixo. Nota-se que não houve acréscimo na precisão devido à aplicação de data augmentation, sendo que a melhor acurácia (87%) foi obtida com 0% de augmentation, ou seja, apenas com os dados reais.

Assim, os resultados destacam que o modelo não respondeu da forma esperada para este indivíduo, indicando a necessidade de mudanças na arquitetura da CGAN para melhor sintetizar as distribuiçoes de dados. Neste contexto, ainda é importante considerar que existe variabilidade entre os indivíduos do dataset, uma vez que distintas respostas neurais podem influenciar a eficácia do modelo, e o modelo proposto ainda pode sintetizar bem os dados para outros indivíduos.

| Augmentation (%) | EEGNet Accuracy |
|-------------------|------------------|
| 0.0               | 0.872464         |
| 5.0               | 0.814917         |
| 10.0              | 0.804749         |
| 15.0              | 0.785894         |
| 20.0              | 0.765700         |
| 30.0              | 0.736607         |
| 40.0              | 0.666667         |
| 50.0              | 0.687259         |
| 70.0              | 0.629693         |
| 100.0             | 0.558611         |



### Métrica Jensen–Shannon (JS)
A divergência de Jensen-Shannon (JS) foi calculada entre os dados reais e os dados gerados pela rede generativa condicional. Essa métrica é utilizada para avaliar a "distância" ou similaridade entre duas distribuições de probabilidade, sendo que  valores menores dessa métrica indicam que as distribuições estão mais próximas, enquanto valores maiores indicam que as distribuições são mais distintas. A comparação foi realizada para cada classe e para cada canal das duas distribuições. Ambos conjuntos de dados reais possuem dimensão (1152, 22), representando 288 amostras para cada classe em cada canal. 


A matriz abaixo, [Figura 3](JS_Metric_Heatmap.png), apresenta os valores da métrica JS calculados para cada classe e eletrodo apenas para o sujeito 3. As cores em azul representam valores mais próximos de 0 e em vermelho representam valores mais próximo de 1. O melhor resultado foi obtido pelo eletrodo FC2, que para todos as classes teve valor menor do que 0.43, ou seja, as distribuições estão próximas uma da outra. O eletrodo C2 gerou valores de JS abaixo de 0.5 para 3 classes ("right hand", "feet" e "tongue"), enquanto Fz obteve resultados satisfatórios para duas classes ("right hand" e "feet"), com valores de JS melhor do que para o eletrodo FC2, indicando boa similaridade entre os dados reais e gerados por essas classe. Os eletrodos CP4 e P2 obteve valores abaixo de 0.5 apenas para uma classe ("left hand" e "right hand"), respectivamente. Em contra partida, os piores resultados foram obtidos pelos eletrodos FC3, C3 e CP3, com valores de JS acima de 0.8, sugerindo que as distribuições geradas estão distantes das distribuições reais.

|![Heatmap](./figure/subject_3/JS_Metric_Heatmap.png "Heatmap da Métrica JS")**Figura 4: Heatmap da métrica JS**|
|:--:| 

### Histogramas de Distribuição
Comparamos a distribuição de frequência dos dados reais com os dados sintéticos a partir do histograma apenas para os eletrodos (FC2, C3, Cz, C2 e C4) [Figura 4](Real_and_Fake_Histogram_Comparison.png). Visualmente, o melhor resultado é observado no histograma do eletrodo FC2, no entanto o resultado do eletrodo C2 é bastante semelhante ao do FC2, indicando, assim como mostrado pela métrica JS, que obtiveram os melhores resultados. Entre esses eletrodos, o C3 e o C4 apresentaram os piores resultados, com distribuições significativamente diferentes.  

Comparando as distribuições de frequência entre os dados reais e sintéticos através do histograma para os eletrodos (FC2, C3, Cz, C2 e C4) [Figura 4](Real_and_Fake_Histogram_Comparison.png). Observa-se que o eletrodo FC2 apresenta o melhor resultado. No entanto, o eletrodo C2 exibe uma semelhança significativa com o FC2, indicando, conforme refletido pela métrica JS, que ambos obtiveram resultados positivos. Por outro lado, os eletrodos C3 e C4 revelaram os piores resultados, exibindo distribuições significativamente diferentes.

|![Histogramas](./figure/subject_3/Real_and_Fake_Histogram_Comparison.png "Histogramas")**Figura 5: Histogramas das distribuições de dados reais e sintéticos**|
|:--:| 

### Comparação dos espaços latentes do terceiro indivíduo

Os manifolds para os dados reais e os dados sintéticos são mostrados na Figura 6 a seguir, onde foi possível observar que com os dados reais os pontos ficaram menos espaçados, podendo haver mistura de classes e indicando que codificador não foi capaz de extratir as características de cada classe. Por outro lado, com os dados sintéticos é possível observar que as classes ficaram mais separadas em dois grupos maiores (roxo e amarelo á esquerda e laranja e azul á direita), mostrando que o manifold gerado pelo codificador conseguiu aprender alguma regra sobre os dados sintéticos. Uma possível explicação para o ocorrido é que o gerador da GAN pode estar enviesando a síntese de alguma classe em especial. 

|![Manifold_dados_reais](./figure/manifolds.png "Manifold_dados_reaiss")**Figura 6: A esquerda manifold dos dados reais e a direita  dos dados sintéticos.**|
|:--:| 

## Comparação da acurácia entre indivíduos 1, 3, 7 e 9
Comparamos a acurácia do classificados para os sujeitos 1, 3, 7 e 9 apenas com os dados reais para verificar variabilidade dos indivíduos no processo de aquisição de dados, e ao adicionar augmentation de ('5%', '10%', '20%', '50%', '70%', '100%' e '200%') para verificar o impacto da variabilidade e também da adição dos dados gerados no classificador [Figura 7](EEGNet_Accuracy_vs_Augmentation.png). 

Ao analisar os resultados apenas com dados reais, observa-se variabilidade relevante entre os sujeitos, com exceção dos sujeitos 3 e 7, que apresentaram valores de acurácia muito próximo. Isso pode ter ocorrido devido a variabilidade de movimentos diferentes entre sujeitos durante a aquisição dos dados. Para esses dois sujeitos (3 e 7) a semelhança no valor da acurácia se mantém apenas com 20% de augmentation, porém houve uma diminuição no valor do acurácia de pelo menos 0.1.  

Percebe-se que existe diminuição significativa nos valores da acurácia ao adicionar os dados sintéticos para todos os sujeitos, com exceção do sujeito 7, que ao adicionar 5% de dados sintéticos apresentou melhor desempenho em relação ao treinar apenas com dados reais. Ou seja, quanto mais adicionamos dados sintéticos, menor é o desempenho do classificador. Isso indica que os dados gerados pelo modelo proposto, pode não ser bom o suficiente para melhorar o desempenho do classificador.

Nota-se ainda que o melhor resultado para esses testes foi o sujeito 7, podendo ser comparável om o sujeito 3. Os piores resultados foram obtidos pelo sujeito 1.  

|![EEGNet_Accuracy_vs_Augmentation](./figure/EEGNet_Accuracy_vs_Augmentation.png "EEGNet_Accuracy_vs_Augmentation")**Figura 7: EEGNet_Accuracy_vs_Augmentation**|
|:--:| 



<!--
## Experimentos, Resultados e Discussão dos Resultados

> Na entrega parcial do projeto (E2), essa seção pode conter resultados parciais, explorações de implementações realizadas e 
> discussões sobre tais experimentos, incluindo decisões de mudança de trajetória ou descrição de novos experimentos, como resultado dessas explorações.

> Na entrega final do projeto (E3), essa seção deverá elencar os **principais** resultados obtidos (não necessariamente todos), que melhor representam o cumprimento
> dos objetivos do projeto.

> A discussão dos resultados pode ser realizada em seção separada ou integrada à seção de resultados. Isso é uma questão de estilo.
> Considera-se fundamental que a apresentação de resultados não sirva como um tratado que tem como único objetivo mostrar que "se trabalhou muito".
> O que se espera da seção de resultados é que ela **apresente e discuta** somente os resultados mais **relevantes**, que mostre os **potenciais e/ou limitações** da metodologia, que destaquem aspectos
> de **performance** e que contenha conteúdo que possa ser classificado como **compartilhamento organizado, didático e reprodutível de conhecimento relevante para a comunidade**. 

 ## Cronograma
> Proposta de cronograma.

|                                       | Setembro     |             | Outubro     |             | Novembro    |             |
|:-------------------------------------:|:------------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|
| **Atividades**                            | 1ª quinzena  | 2ª quinzena | 1ª quinzena | 2ª quinzena | 1ª quinzena | 2ª quinzena |
| **Primeira Entrega**                    | ✔            |             |             |             |             |             |
| Definição do tema                     | ✔            |             |             |             |             |             |
| Levantamento bibliográfico            | ✔            |             |             |             |             |             |
| Escolha da base de dados              |✔            |             |             |             |             |             |
| Escrita da proposta de projeto        | ✔            |             |             |             |             |             |
| **Segunda Entrega**                   |              |             |             |             |             |             |
| Pré-processamento dos dados           |              | X           |             |             |             |             |
| Levantamento bibliográfico           |              | X           |             |             |             |             |
| Reprodução dos resultados do artigo   |              |             | X           | X           |             |             |
| Avaliação dos resultados preliminares |              |             |             | X           |             |             |
| **Entrega Final**                         |              |             |             |             |             |             |
| Consolidação da síntese dos dados     |              |             |             |             | X           |             |
| Resultado das métricas de avaliação   |              |             |             |             | X           | X           |
| Escrita final do projeto              |              |             |             |             |             | X           |
-->
## Dificuldades e limitações
### Dificuldades:
* Convergência do modelo: tivemos dificuldade em encontrar um bom conjunto de hiperparâmetros da rede e pré-processamento de dados para fazer a arquitetura CGAN convergir para um bom resultado.
### Limitações: 
* Acesso a GPU: para treinar uma arquitetura como uma GAN, é necessário ter acesso a bons recursos computacionais. Recursos disponíveis para uso, como o Colab, quase sempre não permite finalizar um treinamento longo, impossibilitando o treinamento de uma GAN para mais épocas.
* Diversidade entre sujeitos: por se tratar de dados de EEG adquiridos por diferentes sujeitos, existe grande variabilidade entre os movimentos realizados ou imaginados. Isso imposibilita, para um projeto de curta duração, utilizar mais de um sujeito para treinamento. É necessário avaliar se usar dados de vários sujeitos é viável, estudar a melhor forma de colocar isso em prática e quais pré-processamento de dados devem ser realizados.

## Conclusão

<!--
> A seção de Conclusão deve ser uma seção que recupera as principais informações já apresentadas no relatório e que aponta para trabalhos futuros.
> Na entrega parcial do projeto (E2) pode conter informações sobre quais etapas ou como o projeto será conduzido até a sua finalização.
> Na entrega final do projeto (E3) espera-se que a conclusão elenque, dentre outros aspectos, possibilidades de continuidade do projeto. --> 

<!-- Até a entrega 2 foram feitos os experimentos preliminares e com os resultados pode-se observar que o modelo está funcional, porém a configuração proposta da CGAN ainda não obteve o resultado esperado. Portanto, para as etapas seguintes alguns testes devem ser feitos para tentar reduzir o número de parâmetros treináveis, realizando convoluções menores, reduzindo a quantidade de camadas intermediárias, alterar o tipo de normalização do dados, o tamanho do kernel, etc. Após estes testes, pretende-se usar as métricas propostas inicialmente que ainda não foram testadas como a divergência KL e a comparação dos espaços latentes usando um autoencoder ou uma PCA usando os dados Reais Vs. Gerados. -->

<!-- Até o momento, os experimentos preliminares foram conduzidos, e os resultados indicaram que o modelo está funcionando. No entanto, a configuração proposta da CGAN ainda não produziu os resultados desejados. Portanto, nas próximas etadas, planeja-se realizar uma série de testes para otimizar o desempenho do modelo. Essas otimizações podem incluir:

- Reduzir o número de parâmetros treináveis: O modelo atual possui 3,513,025 parâmetros treináveis, um número muito alto dado a quantidade de dados de treinamento. Esta redução pode ser alcançada por meio de convoluções menores e redução da quantidade de camadas intermediárias. Com isso, espera-se que a redução do número de parâmetros torne o modelo mais eficiente e mais rápido para treinar.

- Alterar a normalização dos dados: Normalizar os dados de entrada e testar diferentes outras técnicas de normalização de dados, como  Layer Normalization, pode ter um impacto significativo no desempenho do modelo.

- Tamanho do kernel: Ajustar o tamanho do kernel nas camadas de convolução pode influenciar a capacidade do modelo de extrair características relevantes dos dados.

- Métricas de avaliação: Planeja-se usar métricas adicionais, como a divergência de Kullback-Leibler (KL) e a comparação dos espaços latentes. Isso é importante para uma avaliação mais abrangente do modelo.

- Autoencoder ou PCA: Comparar os dados gerados pelo modelo com os dados reais usando técnicas como autoencoders ou Análise de Componentes Principais (PCA) pode fornecer insights valiosos sobre a qualidade das amostras geradas.

Caso a CGAN continue sem produzir resultados satisfatórios, uma opção alternativa é modificar o formato de entrada para matrizes de covariância, conforme sugerido nos estudos de [Marco Congedo et. al](https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1297192) e [Alexandre Barachant et. al](https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1297192). Em último caso, considera-se a substituição do tipo de modelo generativo, como o modelo de difusão proposto por [Giulio Tosato et. al](https://arxiv.org/abs/2303.06068). -->

Este projeto estudou a possibilidade de gerar dados sintéticos de EEG usando uma arquitetura CGAN. De acordo com os resultados apresentados, foi possível sintetizar os dados e obter uma boa convergência no treinamento do modelo generativo adversário, como mostrado na Figura 3.

 Os resultados indicam que alguns canais da base de dados tiveram uma melhor distribuição sintetizada pela arquitetura, como foi o caso do eletrodo FC2 mostrado na métrica de JS e nos histogramas (Figuras 4 e 5), ao passo que outros canais não apresentaram o mesmo resultado. 

Analisando a métrica de acurácia, observou-se que ao executar o experimento usando *data augmentation* no classificador, observou-se que a adição de dados sintéticos não ajudou significativamente a melhorar o desempenho do modelo. Apenas o sujeito 7 obteve uma pequena melhora de 1% ao adicionar 5% de dados sintéticos. 

Por fim, com a comparação dos espaços latentes, levantou-se a hipótese de que o gerador esteja enviesando a sintetização de algumas classes, gerando dados com algumas distribuições melhores do que outras. Isso pode ter se refletido no resultado da acurácia durante o processo de data augmentation.

Como trabalhos futuros, alguns caminhos possíveis são:
-  Refinar a arquitetura da GAN com mais testes como tipo de camada, funções de ativação, funções de loss e otimizadores;
- Utilizar matrizes de covariância como dados de entrada e geometria riemaniana para o mapeamento dos dados em outro espaço, como proposto por [Wilson, Daniel et al.](https://arxiv.org/pdf/2212.10426.pdf)
-  Considerar outras técnicas de geração de dados, como modelo de difusão.

<!-- Caso ainda assim a CGAN não apresente bons resultados, um caminho alternativo seria alterar o formato da entrada para matrizes de covariância, como proposto nos trabalhos de [Marco Congedo et. al](https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1297192) e [Alexandre Barachant et. al](https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1297192). Em último caso seria tentar trocar o tipo de modelo generativo, por exemplo o modelo de difusão proposto por [Giulio Tosato et. al](https://arxiv.org/abs/2303.06068).  -->


## Apêndice A - Testes Realizados no Treinamento da GAN

|![grid_plot_loss](./figure/grid_plot_loss.png "grid_plot_loss")**Figura 8: Grid plot dos testes realizados no treinamento da GAN**|
|:--:| 

## Apêndice B - Heatmap da Métrica JS para indivíduos 1, 7 e 9

![grid_plot_loss](./figure/JS_Metric_Heatmap_sub1.png "grid_plot_loss")

![grid_plot_loss](./figure/JS_Metric_Heatmap_sub7.png "grid_plot_loss")

|![grid_plot_loss](./figure/JS_Metric_Heatmap_sub9.png "grid_plot_loss")**Figura 9: JS Metrics para sujeitos 1, 7 e 9**|
|:--:| 



## Referências Bibliográficas
- Tese Sarah Negreiros de Carvalho Leite - Contribuições ao desenvolvimento de interfaces cérebro-computador baseadas em potenciais evocados visualmente em regime estacionário

  Tese: (https://doi.org/10.47749/T/UNICAMP.2016.970748)

- Augmenting EEG with Generative Adversarial Networks Enhances Brain Decoding Across Classifiers and Sample Sizes

  Paper: (https://escholarship.org/uc/item/9gz8g908)
  Git: (https://github.com/AutoResearch/EEG-GAN)

- EEG data augmentation for emotion recognition with a multiple generator conditional Wasserstein GAN

  Paper: (https://link.springer.com/article/10.1007/s40747-021-00336-7)

- EEG-GAN: Generative adversarial networks for electroencephalograhic (EEG) brain signals

  Paper: (https://arxiv.org/abs/1806.01875)
  Git: (https://github.com/aung2phyowai/GAN)

- EEG Synthetic Data Generation Using Probabilistic Diffusion Models

  Paper: (https://arxiv.org/abs/2303.06068)

- Riemannian geometry for EEG-based brain-computer interfaces; a primer and a review
  
  Paper: (https://www.tandfonline.com/doi/full/10.1080/2326263X.2017.1297192)

- Multiclass Brain–Computer Interface Classification by Riemannian Geometry
  
  Paper: (https://ieeexplore.ieee.org/document/6046114)

-  EEGNet: A Compact Convolutional Network for EEG-based Brain-Computer Interfaces. 
  Paper: (https://arxiv.org/pdf/1611.08024.pdf)
  Git: (https://github.com/arkanivasarkar/EEG-Data-Augmentation-using-Variational-Autoencoder)

