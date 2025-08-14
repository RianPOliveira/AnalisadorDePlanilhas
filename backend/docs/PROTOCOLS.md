# 📡 Documentação Técnica dos Protocolos

## Visão Geral

O Mangaba AI implementa dois protocolos fundamentais para comunicação e gerenciamento de contexto:

- **A2A (Agent-to-Agent)**: Protocolo de comunicação entre agentes
- **MCP (Model Context Protocol)**: Protocolo de gerenciamento de contexto

## 🔗 Protocolo A2A (Agent-to-Agent)

### Arquitetura

O protocolo A2A permite que múltiplos agentes se comuniquem de forma estruturada e eficiente.

#### Tipos de Mensagem

```python
class MessageType(Enum):
    REQUEST = "request"        # Requisições entre agentes
    RESPONSE = "response"      # Respostas a requisições
    BROADCAST = "broadcast"    # Mensagens para múltiplos agentes
    NOTIFICATION = "notification"  # Notificações assíncronas
    ERROR = "error"           # Mensagens de erro
```

#### Estrutura de Mensagem

```python
class A2AMessage:
    message_id: str          # ID único da mensagem
    message_type: MessageType # Tipo da mensagem
    sender_id: str           # ID do agente remetente
    target_id: str           # ID do agente destinatário (opcional para broadcast)
    content: dict            # Conteúdo da mensagem
    timestamp: datetime      # Timestamp da criação
    correlation_id: str      # ID para correlacionar request/response
```

#### Funcionalidades Principais

1. **Registro de Handlers**
   ```python
   protocol.register_handler(MessageType.REQUEST, handler_function)
   ```

2. **Envio de Mensagens**
   ```python
   protocol.send_message(message)
   ```

3. **Criação de Requisições**
   ```python
   request = protocol.create_request(target_id, content)
   ```

4. **Criação de Broadcasts**
   ```python
   broadcast = protocol.create_broadcast(content)
   ```

### Implementação no Mangaba

O `MangabaAgent` implementa handlers específicos:

- `handle_mangaba_request`: Processa requisições recebidas
- `handle_mangaba_response`: Processa respostas recebidas

#### Ações Suportadas

- `chat`: Executa chat com mensagem
- `analyze`: Executa análise de texto
- `translate`: Executa tradução
- `get_context`: Retorna resumo do contexto

## 🧠 Protocolo MCP (Model Context Protocol)

### Arquitetura

O protocolo MCP gerencia contexto de forma inteligente e estruturada.

#### Tipos de Contexto

```python
class ContextType(Enum):
    CONVERSATION = "conversation"  # Conversas e diálogos
    TASK = "task"                 # Tarefas específicas
    MEMORY = "memory"             # Memórias de longo prazo
    SYSTEM = "system"             # Informações do sistema
```

#### Prioridades de Contexto

```python
class ContextPriority(Enum):
    HIGH = "high"      # Contexto crítico (sempre preservado)
    MEDIUM = "medium"  # Contexto importante
    LOW = "low"        # Contexto opcional
```

#### Estrutura de Contexto

```python
class MCPContext:
    context_id: str          # ID único do contexto
    context_type: ContextType # Tipo do contexto
    content: dict            # Conteúdo do contexto
    priority: ContextPriority # Prioridade do contexto
    tags: List[str]          # Tags para categorização
    timestamp: datetime      # Timestamp da criação
    expires_at: datetime     # Data de expiração (opcional)
    metadata: dict           # Metadados adicionais
```

#### Sessões MCP

```python
class MCPSession:
    session_id: str          # ID único da sessão
    created_at: datetime     # Data de criação
    last_accessed: datetime  # Último acesso
    metadata: dict           # Metadados da sessão
```

### Funcionalidades Principais

1. **Gerenciamento de Contexto**
   ```python
   mcp.add_context(context, session_id)
   mcp.get_context(context_id)
   mcp.update_context(context_id, new_content)
   mcp.remove_context(context_id)
   ```

2. **Busca de Contexto**
   ```python
   contexts = mcp.find_contexts_by_tag("conversation")
   contexts = mcp.find_contexts_by_type(ContextType.TASK)
   contexts = mcp.get_relevant_contexts(query, max_results=5)
   ```

3. **Gerenciamento de Sessões**
   ```python
   session = mcp.create_session()
   contexts = mcp.get_session_contexts(session_id)
   ```

### Implementação no Mangaba

O `MangabaAgent` integra MCP automaticamente:

1. **Chat com Contexto**
   - Adiciona mensagens do usuário ao contexto
   - Busca contexto relevante para enriquecer prompts
   - Armazena respostas da IA no contexto

2. **Análise e Tradução**
   - Armazena resultados como contexto de tarefa
   - Permite referência futura aos resultados

3. **Resumo de Contexto**
   - Agrupa contextos por tipo
   - Fornece visão geral da sessão atual

## 🔄 Integração dos Protocolos

### Fluxo de Comunicação

1. **Agente A** envia requisição via A2A para **Agente B**
2. **Agente B** processa requisição usando contexto MCP
3. **Agente B** envia resposta via A2A para **Agente A**
4. **Agente A** armazena resposta no contexto MCP

### Benefícios da Integração

- **Contexto Compartilhado**: Agentes podem compartilhar contexto
- **Comunicação Inteligente**: Respostas baseadas em histórico
- **Escalabilidade**: Suporte a múltiplos agentes
- **Persistência**: Contexto mantido entre sessões

## 🛠️ Exemplos de Uso

### Comunicação Básica A2A

```python
# Agente 1 envia requisição
request = agent1.send_agent_request(
    target_agent_id=agent2.agent_id,
    action="analyze",
    params={
        "text": "Texto para análise",
        "instruction": "Analise o sentimento"
    }
)
```

### Contexto Avançado MCP

```python
# Chat com contexto automático
agent.chat("Meu nome é João")  # Armazenado no contexto
agent.chat("Qual minha profissão?")  # Usa contexto anterior

# Busca contexto específico
contexts = agent.mcp.find_contexts_by_tag("user_info")
```

### Broadcast com Contexto

```python
# Broadcast que será armazenado no contexto de todos os agentes
result = agent.broadcast_message(
    message="Reunião às 15h",
    tags=["meeting", "schedule"]
)
```

## 🔧 Configuração e Personalização

### Handlers Customizados

```python
def custom_handler(message: A2AMessage):
    # Lógica personalizada
    response = process_custom_action(message.content)
    return agent.a2a_protocol.create_response(message, response, True)

# Registrar handler
agent.a2a_protocol.register_handler(MessageType.REQUEST, custom_handler)
```

### Contexto Personalizado

```python
# Criar contexto customizado
custom_context = MCPContext.create(
    context_type=ContextType.MEMORY,
    content={"key": "value"},
    priority=ContextPriority.HIGH,
    tags=["custom", "important"]
)

agent.mcp.add_context(custom_context, agent.current_session_id)
```

## 📊 Monitoramento e Debug

### Logs A2A

```python
# Logs automáticos para todas as operações A2A
# 📤 Requisição enviada para agent_123: chat
# 📨 Resposta de agent_456: resultado...
# 📢 Broadcast enviado: mensagem...
```

### Logs MCP

```python
# Logs automáticos para operações MCP
# 💬 Chat: mensagem... → resposta...
# 🔍 Análise: texto... → resultado...
# 🌐 Tradução: texto... → idioma
```

### Debugging

```python
# Verificar estado dos protocolos
print(f"Agent ID: {agent.agent_id}")
print(f"MCP Enabled: {agent.mcp_enabled}")
print(f"Session ID: {agent.current_session_id}")

# Verificar contextos
contexts = agent.mcp.get_session_contexts(agent.current_session_id)
print(f"Contextos ativos: {len(contexts)}")
```

## 🚀 Próximos Passos

### Funcionalidades Planejadas

1. **Persistência**: Salvar contexto em banco de dados
2. **Rede de Agentes**: Descoberta automática de agentes
3. **Balanceamento**: Distribuição de carga entre agentes
4. **Segurança**: Autenticação e autorização
5. **Métricas**: Monitoramento de performance

### Extensibilidade

Os protocolos foram projetados para serem extensíveis:

- Novos tipos de mensagem A2A
- Novos tipos de contexto MCP
- Handlers personalizados
- Estratégias de busca customizadas
- Políticas de expiração flexíveis