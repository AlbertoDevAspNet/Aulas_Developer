# Aulas_Developer
Conceitos centrais
Pull Request (PR): mecanismo para propor alterações em um repositório, permitindo revisão antes da integração.

Code Review: processo de análise do código submetido, garantindo qualidade, consistência e aprendizado coletivo.

Conflitos de merge: inevitáveis em desenvolvimento colaborativo; precisam ser resolvidos com justificativas técnicas e documentação clara.

criar nova branch
git checkout -b feature/nova-funcionalidade

fazer alterações no código e salvar 
# editar arquivos...
git add .
git commit -m "Implementa nova funcionalidade X"

Enviar a branch para o repositório remoto

git push origin feature/nova-funcionalidade

 Abrir um Pull Request(PR)
 Resolver conflitos de merge se houver 
 git checkout main
git pull origin main
git merge feature/nova-funcionalidade
# resolver conflitos manualmente nos arquivos
git add .
git commit -m "Resolve conflitos entre main e feature/nova-funcionalidade"

Atualizar o PR com as correções

git push origin feature/nova-funcionalidade

Revisão final e merge
Após aprovação no Code Review, o PR é aceito.

O merge pode ser feito via interface da plataforma ou pelo terminal:

git checkout main
git merge feature/nova-funcionalidade
git push origin main




 

