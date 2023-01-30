
def cpf_valido(numero_cpf):
    return len(numero_cpf) == 11
        
def nome_valido(nome):
    return nome.isalpha()
  

def rg_valido(numero_rg):
    return len(numero_rg) == 9
       


def validate_celular(self, celular):
    if len(celular) < 11:
        raise serializers.ValidationError("O celular deve ter, no mínimo, 11 dígitos!")
    return celular
 