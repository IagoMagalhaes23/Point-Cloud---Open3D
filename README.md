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

## Referências
- https://betterprogramming.pub/introduction-to-point-cloud-processing-dbda9b167534
- https://github.com/Chim-SO/pointcloudprocessing
