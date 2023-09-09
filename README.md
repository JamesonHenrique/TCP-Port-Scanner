

```markdown
# Scanner de Portas

Este é um simples scanner de portas em Python que permite verificar se as portas de um determinado endereço IP estão abertas ou fechadas. O programa utiliza a biblioteca `socket` para realizar a verificação das portas.

## Como Usar

1. Clone o repositório para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/scanner-de-portas.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd scanner-de-portas
   ```

3. Execute o programa Python, fornecendo o endereço IP que você deseja escanear como entrada:
   ```bash
   python scanner.py
   ```

   O programa solicitará que você insira o endereço IP alvo.

4. O scanner irá verificar as portas de 1 a 1024 no endereço IP especificado e exibirá as portas abertas, se houver alguma.

## Exemplo de Uso

```
Digite o IP: 192.168.1.1
Procurando portas...

80 - Porta aberta
443 - Porta aberta

Scan finalizada
```

## Notas

- O programa verifica portas no intervalo de 1 a 1024, mas você pode ajustar esse intervalo no código-fonte, se necessário.

- Certifique-se de que você tem permissão legal para escanear o endereço IP fornecido. Escanear IPs sem autorização adequada pode ser ilegal em algumas jurisdições.

## Contribuições

Contribuições são bem-vindas! Se você quiser melhorar este projeto de alguma forma, sinta-se à vontade para criar um fork e enviar um pull request com suas melhorias.

