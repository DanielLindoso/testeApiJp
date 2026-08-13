from fastapi import APIRouter, status

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_contact(payload: dict):
    # BUG INTENCIONAL:
    # Não existe validação dos campos.
    return {
        "message": "Contato recebido",
        "data": payload,
    }
