# Point-Cloud---Open3D

# Resumo
Repositório para estudo de Point Clouds em Python utilizando a lib Open3D.

## Introdução a Point Clouds
Uma nuvem de pontos é um conjunto de pontos que representa a cena no mundo real ou objetos no espaço. É uma representação discreta de objetos e cenas geométricas.
Suas aplicações estão por toda parte, como: robótica, veículos autônomos, sistemas de assistência, saúde, etc. Uma nuvem de pontos é uma representação 3D adequada para processar dados do mundo real, especialmente quando a geometria da cena/objetos é necessária, como a distância, a forma e o tamanho dos objetos.

### random_points.py
Geralmente, as nuvens de pontos são representadas por (n × 3) matrizes onde n é o número de pontos.
Então, nesse arquivo .py é criado uma nuvem de pontos com 50 pontos aleatórios: <br>
![image](https://user-images.githubusercontent.com/65053026/222008755-4ebc7ffa-5ce1-47f2-99e2-a4491fe92e98.png)
<br>
Libs:
- Numpy
- MatplotLib

### sampling.py
Importando um modelo 3D de um coelho da lib Open3D. <br>
![image](https://user-images.githubusercontent.com/65053026/222009089-cfc7b99a-384e-41ee-bc66-9309b4cee419.png)
<br>
Representação da nuvem de pontos do modelo 3D. <br>
![image](https://user-images.githubusercontent.com/65053026/222009212-07280a0b-a458-465a-9ca4-0f8450b8dc1e.png)
<br>
Libs:
- Open3D

### rgbd.py
Os dados RGB-D são coletados usando sensores RGB-D (como o Microsoft Kinect) que fornecem simultaneamente uma imagem RGB e uma imagem de profundidade. Os sensores RGB-D estão envolvidos em muitas aplicações, como navegação interna, prevenção de obstáculos, etc. Como a imagem RGB fornece a cor do pixel, cada pixel da imagem de profundidade indica sua distância da câmera. <br>
![image](https://user-images.githubusercontent.com/65053026/222009399-9f58a402-3d96-42fd-9c1e-82371ef355fc.png)
<br>
Libs:
- Open3D

### numpyForOpen3d.py
Convertendo objeto Open3D para Numpy. <br>
![image](https://user-images.githubusercontent.com/65053026/222009573-0429aced-fa45-4ebb-bc29-3ff3b7cf6390.png)
<br>
Libs:
- Numpy
- MatplotLib
- Open3D

## Imagens em profundidade
Uma imagem de profundidade (também chamada de mapa de profundidade) é uma imagem em que cada pixel fornece seu valor de distância em relação ao sistema de coordenadas do sensor. <br>

### Plotar nuvem de pontos de uma imagem em profundidade
Após ler e carregar uma imagem em profundidade, podemos realizar a estimativa de sua nuvem de pontos. Para isso, a primeira etapa é calibrar a câmera de profundidade para estimar a matriz da câmera e, em seguida, usá-la para calcular a nuvem de pontos. A nuvem de pontos obtida também é chamada de nuvem de pontos 2,5D, pois é estimada a partir de uma projeção 2D (imagem de profundidade) em vez de sensores 3D, como sensores a laser.

Calibrar uma câmera significa estimar os parâmetros da lente e do sensor encontrando os coeficientes de distorção e a matriz da câmera, também chamados de parâmetros intrínsecos.

Calcular a nuvem de pontos aqui significa transformar o pixel de profundidade do sistema de coordenadas 2D da imagem de profundidade para o sistema de coordenadas 3D da câmera de profundidade ( x, y e z ).

### pointcloud_from_depth.py
Carregando uma imagem em profundidade e a nuvem de pontos correspondente com MatplotLib em tons de cinza.
![image](https://user-images.githubusercontent.com/65053026/222753682-31d2137b-93de-4154-a8da-96262c0c8e1b.png) <br>
![image](https://user-images.githubusercontent.com/65053026/222754057-a6763064-aebe-4c69-b61c-c914f6c2f761.png) <br>
Libs:
- Imageio
- Numpy
- MatplotLib
- Open3D

### colored_pointcloud_from_depth.py
Carregando uma imagem em profundidade e a nuvem de pontos correspondente com MatplotLib com cores.
![image](https://user-images.githubusercontent.com/65053026/222754215-823c907c-ee50-4892-90f2-10182fea1452.png) <br>
![image](https://user-images.githubusercontent.com/65053026/222754447-3b6cc0a9-7f97-4bc4-97ff-38b49db56ee3.png) <br>
Libs:
- Imageio
- Numpy
- MatplotLib
- Open3D

## Detecção de parede
Nesta aula tentei realizar a detecção da uma parede em uma imagem de profundidade. Ainda existem alguns erros e claro o projeto pode ser melhorado, ele se basea no exemplo de deteccção do chão. Com base nas posições minímas e máximas das coordernadas X, Y e Z é possível identificar tais regiões.

### computer_vision_coordinate_system.py
Plotando pontos minímos e máximos das coordernadas X, Y e Z.
![image](https://user-images.githubusercontent.com/65053026/223578096-493678ea-894f-453f-b836-d185ea6f60f3.png) <br>
Libs:
- Numpy
- Open3D
- ImageIo
- MatplotLib

### parede_detection.py
Detecando a parede através de uma imagem de profundidade.
![image](https://user-images.githubusercontent.com/65053026/223578421-e961a2e2-a1f1-4d83-b7d7-304442b45cce.png) <br>
Libs:
- Numpy
- Open3D

### organized_pointcloud.py
Organizando a identificação da parede com a imagem em profundidade.
![Parede_DepthImage](https://user-images.githubusercontent.com/65053026/223578607-7adc3251-d963-4090-bf60-96f14701c97d.png) <br>
Libs:
- ImageIO
- Numpy
- MatplotLib
- Open3D

## Filtragem de nuvem de pontos
As nuvens de pontos computadas ou reunidas podem às vezes ser ruidosas devido à natureza dos scanners 3D usados ​​(como scanners de luz estruturada) ou da cena capturada (inclui materiais que absorvem luzes infravermelhas). Por outro lado, alguns algoritmos e/ou técnicas de visão computacional são sensíveis ao ruído, como estimar normais de superfície e mudanças de curvatura. - Chayma Zatout

### Filtro de passagem
O filtro Pass-through aplica restrições aos dados de entrada, que geralmente são limites ou intervalos. Para nuvens de pontos, um ponto passa pelo filtro se satisfizer as restrições que são principalmente intervalos ao longo de um ou mais eixos. Para reduzir o ruído, o intervalo geralmente é fixado de acordo com a natureza e o estado do dispositivo de entrada: os dados de profundidade são mais precisos dentro do intervalo e tornam-se mais ruidosos caso contrário. O filtro pass-through pode ser usado não apenas para filtrar a entrada do ruído, mas também para reduzir dados como considerar os pontos mais próximos.

### Redução de amostragem
O downsampling das nuvens de pontos consiste em reduzir o número de pontos. Geralmente é aplicado para reduzir o tempo de execução da etapa de processamento ou para selecionar um número exato de pontos para treinamento, por exemplo.

### Filtros de remoção de outliers
- A remoção de valores discrepantes do raio é um filtro condicional que remove todos os pontos que tenham menos do que um determinado número de vizinhos dentro de uma esfera de um determinado raio.
- O filtro de remoção de outliers estatísticos remove pontos que estão mais distantes de seus vizinhos. Para cada ponto, a distância média dele para todos os seus vizinhos é calculada. Então, se a distância média do ponto estiver fora de um intervalo definido pela média e desvio padrão das distâncias globais, o ponto é um valor discrepante.




### crop_pointcloud_o3d.py

Libs:
- 

### downsampling.py

Libs:
- 

### passthrough_filter_np.py

Libs:
- 

### point_cloud_filtering.py

Libs:
- 

## Segmentação de nuvem de pontos
Em geral, a segmentação de dados visa reagrupar os dados em grupos não sobrepostos. Na segmentação de nuvem de pontos, esses grupos podem corresponder a regiões: objetos ou parte deles, superfícies, planos, etc. . Neste tutorial, estamos interessados ​​em métodos baseados em clustering. Os algoritmos de agrupamento são implementados em muitas APIs de aprendizado de máquina, incluindo o Scikit-learn, que usaremos neste tutorial. - Chayma Zatout

### K-means
K-means é um algoritmo baseado em centroide. Ele divide as amostras de entrada em K grupos separados com variância igual enquanto minimiza as distâncias entre os pontos.

### DBSCAN
O algoritmo DBSCAN busca separar as amostras em clusters de alta densidade com áreas de baixa densidade. O número de clusters não precisa ser definido previamente. O DBSCAN é robusto a ruído: durante o agrupamento, os outliers são detectados e negligenciados e, portanto, o processo de agrupamento não é afetado por eles.

### Projection_clustering.py
- Visualização com K-means
![image](https://user-images.githubusercontent.com/65053026/224492020-11aaeb20-c13c-42a6-94f6-03b2c92e0f51.png) <br>
- Visualização com DBSCAN
![image](https://user-images.githubusercontent.com/65053026/224491914-8f1103d1-d59b-4bc4-ad85-4c1801746a7a.png) <br>
- Visualização da projeção
![image](https://user-images.githubusercontent.com/65053026/224491958-d99f0263-10d4-42cd-9205-fb55becfbebe.png) <br>

Libs:
- Numpy
- Open3D
- SKLearn
- MatplotLib

### clustering.py
- Segmentação utilizando K-means
![image](https://user-images.githubusercontent.com/65053026/224492179-3cf2ba8f-92bf-4150-80b8-f7e3ce1731b8.png) <br>

Libs:
- Numpy
- Open3D
- SKLearn
- MatplotLib

## Referências
- https://betterprogramming.pub/introduction-to-point-cloud-processing-dbda9b167534
- https://github.com/Chim-SO/pointcloudprocessing
- https://docs.opencv.org/4.6.0/dc/dbb/tutorial_py_calibration.html
- https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html
- http://www.open3d.org/docs/0.7.0/python_api/open3d.geometry.crop_point_cloud.html?highlight=crop_point_cloud#open3d.geometry.crop_point_cloud
- https://betterprogramming.pub/point-cloud-filtering-in-python-e8a06bbbcee5
