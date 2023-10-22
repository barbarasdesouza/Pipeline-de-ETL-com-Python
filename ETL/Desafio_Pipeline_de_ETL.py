import pandas as pd
import matplotlib.pyplot as plt

# Extração de dados de sensores (valores fictícios)
data = {
    'timestamp': ['2023-10-19 08:00:00', '2023-10-19 09:00:00', '2023-10-19 10:00:00'],
    'temperatura': [25.2, 26.1, 27.5],
    'umidade': [50, 48, 45],
    'qualidade_ar': [30, 35, 40]
}

# Criando um DataFrame do pandas a partir dos dados
df = pd.DataFrame(data)

# Visualizando os dados
print("Dados dos sensores:")
print(df)

# Transformação: Análise de tendências de temperatura, umidade e qualidade do ar
plt.figure(figsize=(10, 5))
plt.plot(df['timestamp'], df['temperatura'], label='Temperatura (°C)')
plt.plot(df['timestamp'], df['umidade'], label='Umidade (%)')
plt.plot(df['timestamp'], df['qualidade_ar'], label='Qualidade do Ar (IAQ)')
plt.xlabel('Horário')
plt.ylabel('Valores')
plt.title('Tendências Ambientais')
plt.legend()
plt.grid(True)

# Salvando o gráfico em um arquivo ou exibindo
plt.savefig('tendencias_ambientais.png')  # Salvar em um arquivo
plt.show()  # Exibir o gráfico na tela

