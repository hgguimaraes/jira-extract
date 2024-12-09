from flask import Flask, request, jsonify  # Corrigido: importações completas
from flask_cors import CORS
from jira_service import JiraService  # Certifique-se de que o módulo jira_service está configurado corretamente

# Inicialização do Flask e CORS
app = Flask(__name__)
CORS(app)

# Inicialização do serviço JIRA
jira_service = JiraService()

@app.route('/api/extract-comments', methods=['POST'])
def extract_comments():
    """
    Rota para extrair comentários do JIRA com base em um intervalo de datas.
    """
    try:
        data = request.json
        start_date = data.get('startDate')
        end_date = data.get('endDate')
        
        # Validação dos dados de entrada
        if not start_date or not end_date:
            return jsonify({'success': False, 'error': 'Start date and end date are required'}), 400
            
        # Extração de comentários
        result = jira_service.extract_comments(start_date, end_date)
        return jsonify({'success': True, 'data': result}), 200
    except ValueError as ve:
        return jsonify({'success': False, 'error': f'Invalid data format: {str(ve)}'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Configuração do servidor
    app.run(port=5000, debug=True)  # Adicionado debug para ambiente de desenvolvimento
