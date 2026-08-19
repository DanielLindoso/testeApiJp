from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_contact(payload: dict):

    if not payload.get("name") or not payload.get("email") or not payload.get("message"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nome, email e mensagem são obrigatórios",
        )

    return {
        "message": "Contato recebido",
        "data": payload,
    }