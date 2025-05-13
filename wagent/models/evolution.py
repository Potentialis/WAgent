from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List, Any


class MessageContextInfo(BaseModel):
    messageSecret: str


# Base class for media messages sharing common fields
class BaseMediaMessage(BaseModel):
    url: str
    mimetype: str
    fileSha256: str
    fileLength: str
    mediaKey: str
    fileEncSha256: str
    directPath: str
    mediaKeyTimestamp: str


class AudioMessage(BaseMediaMessage):
    seconds: int
    ptt: bool
    waveform: Optional[str] = None


class ImageMessage(BaseMediaMessage):
    height: int
    width: int
    jpegThumbnail: Optional[str] = None
    scansSidecar: Optional[str] = None
    scanLengths: Optional[List[int]] = None


class VideoMessage(BaseMediaMessage):
    seconds: int
    height: int
    width: int
    # Optional fields specific to video
    jpegThumbnail: Optional[str] = None
    contextInfo: Optional[Any] = None  # can be dict or other
    streamingSidecar: Optional[str] = None
    gifPlayback: Optional[bool] = None
    gifAttribution: Optional[str] = None


class StickerMessage(BaseMediaMessage):
    isAnimated: bool
    stickerSentTs: Optional[str] = None
    isAvatar: bool
    isAiSticker: bool
    isLottie: bool


class DocumentMessage(BaseMediaMessage):
    pageCount: int
    fileName: str
    thumbnailDirectPath: Optional[str] = None
    thumbnailSha256: Optional[str] = None
    thumbnailEncSha256: Optional[str] = None
    jpegThumbnail: Optional[str] = None
    thumbnailHeight: Optional[int] = None
    thumbnailWidth: Optional[int] = None


class LocationMessage(BaseModel):
    degreesLatitude: float
    degreesLongitude: float
    jpegThumbnail: Optional[str] = None


class ContactMessage(BaseModel):
    displayName: str
    vcard: str


class PollOption(BaseModel):
    optionName: str


class PollCreationMessageV3(BaseModel):
    name: str
    options: List[PollOption]
    selectableOptionsCount: int


class EventMessage(BaseModel):
    isCanceled: bool
    name: str
    startTime: str


class Message(BaseModel):
    conversation: Optional[str] = None
    audioMessage: Optional[AudioMessage] = None
    imageMessage: Optional[ImageMessage] = None
    videoMessage: Optional[VideoMessage] = None
    stickerMessage: Optional[StickerMessage] = None
    locationMessage: Optional[LocationMessage] = None
    contactMessage: Optional[ContactMessage] = None
    documentMessage: Optional[DocumentMessage] = None
    pollCreationMessageV3: Optional[PollCreationMessageV3] = None
    eventMessage: Optional[EventMessage] = None
    messageContextInfo: Optional[MessageContextInfo] = None
    base64: Optional[str] = None


class KeyInfo(BaseModel):
    remoteJid: str
    fromMe: bool
    id: str


class Data(BaseModel):
    key: KeyInfo
    pushName: str
    status: str
    message: Message
    messageType: str
    messageTimestamp: int
    instanceId: str
    source: str
    contextInfo: Optional[Any] = None


class EvoWebhookPayload(BaseModel):
    event: str
    instance: str
    data: Data
    destination: str
    date_time: datetime
    sender: str
    server_url: str
    apikey: str
